#import <Foundation/Foundation.h>
#import <CoreImage/CoreImage.h>
#import <CoreGraphics/CoreGraphics.h>
#import <ImageIO/ImageIO.h>
#import <UniformTypeIdentifiers/UniformTypeIdentifiers.h>
#import <stdio.h>

BOOL processPhoto(NSString *inPath, NSString *outPath, double noiseLevel, double denoiseSharpness, double finalSharpness) {
    NSURL *inUrl = [NSURL fileURLWithPath:inPath];
    CIImage *input = [CIImage imageWithContentsOfURL:inUrl];
    if (!input) {
        printf("ERROR: Could not load %s\n", [inPath UTF8String]);
        return NO;
    }
    
    CGRect extent = [input extent];
    int origW = (int)extent.size.width;
    int origH = (int)extent.size.height;
    
    // 1. Edge-preserving noise reduction
    CIFilter *denoise = [CIFilter filterWithName:@"CINoiseReduction"];
    [denoise setValue:input forKey:kCIInputImageKey];
    [denoise setValue:@(noiseLevel) forKey:@"inputNoiseLevel"];
    [denoise setValue:@(denoiseSharpness) forKey:@"inputSharpness"];
    CIImage *denoised = [denoise outputImage];
    
    // 2. Luminance sharpening to recover micro-contrast on edges without halos
    CIImage *finalCI = denoised;
    if (finalSharpness > 0.0) {
        CIFilter *sharpen = [CIFilter filterWithName:@"CISharpenLuminance"];
        [sharpen setValue:denoised forKey:kCIInputImageKey];
        [sharpen setValue:@(finalSharpness) forKey:@"inputSharpness"];
        [sharpen setValue:@(1.2) forKey:@"inputRadius"];
        finalCI = [sharpen outputImage];
    }
    
    // Render using hardware-accelerated context
    CIContext *ctx = [CIContext contextWithOptions:@{kCIContextUseSoftwareRenderer: @NO}];
    CGImageRef cgImg = [ctx createCGImage:finalCI fromRect:extent];
    if (!cgImg) {
        printf("ERROR: Rendering failed for %s\n", [inPath UTF8String]);
        return NO;
    }
    
    size_t outW = CGImageGetWidth(cgImg);
    size_t outH = CGImageGetHeight(cgImg);
    if (outW != origW || outH != origH) {
        printf("CRITICAL ERROR: Dimension mismatch! Orig %dx%d vs Out %zux%zu\n", origW, origH, outW, outH);
        CGImageRelease(cgImg);
        return NO;
    }
    
    // Determine UTType from extension
    NSString *ext = [[outPath pathExtension] lowercaseString];
    CFStringRef uti = (__bridge CFStringRef)UTTypePNG.identifier;
    NSDictionary *options = nil;
    
    if ([ext isEqualToString:@"jpg"] || [ext isEqualToString:@"jpeg"]) {
        uti = (__bridge CFStringRef)UTTypeJPEG.identifier;
        options = @{(__bridge NSString *)kCGImageDestinationLossyCompressionQuality: @(1.0)};
    } else if ([ext isEqualToString:@"webp"]) {
        uti = (__bridge CFStringRef)UTTypeWebP.identifier;
    }
    
    NSURL *outUrl = [NSURL fileURLWithPath:outPath];
    CGImageDestinationRef dest = CGImageDestinationCreateWithURL((__bridge CFURLRef)outUrl, uti, 1, NULL);
    if (!dest) {
        printf("ERROR: Could not create destination for %s\n", [outPath UTF8String]);
        CGImageRelease(cgImg);
        return NO;
    }
    
    CGImageDestinationAddImage(dest, cgImg, (__bridge CFDictionaryRef)options);
    BOOL success = CGImageDestinationFinalize(dest);
    CFRelease(dest);
    CGImageRelease(cgImg);
    
    if (success) {
        printf("SUCCESS: %s -> %s [%dx%d]\n", [[inPath lastPathComponent] UTF8String], [[outPath lastPathComponent] UTF8String], origW, origH);
    } else {
        printf("ERROR: Finalize failed for %s\n", [outPath UTF8String]);
    }
    return success;
}

int main() {
    @autoreleasepool {
        // Test 1: Project 06 Photo 2 (In-situ on wood block)
        processPhoto(
            @"/Users/morganjanot/.gemini/antigravity/brain/04838ef3-4249-4209-97cb-1440ffec4bcd/.user_uploaded/media_1790804190821.png",
            @"/Users/morganjanot/.gemini/antigravity/scratch/test_refined_0821.png",
            0.045, 0.55, 0.35
        );
        // Test 2: Project 06 Photo 1 (Floating on pure black)
        processPhoto(
            @"/Users/morganjanot/.gemini/antigravity/brain/04838ef3-4249-4209-97cb-1440ffec4bcd/.user_uploaded/media_1790804190785.png",
            @"/Users/morganjanot/.gemini/antigravity/scratch/test_refined_0785.png",
            0.035, 0.50, 0.30
        );
    }
    return 0;
}
