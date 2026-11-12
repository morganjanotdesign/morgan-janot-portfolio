#import <Foundation/Foundation.h>
#import <CoreImage/CoreImage.h>
#import <CoreGraphics/CoreGraphics.h>
#import <ImageIO/ImageIO.h>
#import <UniformTypeIdentifiers/UniformTypeIdentifiers.h>
#import <stdio.h>

BOOL processImageFile(NSString *inPath, NSString *outPath, double noiseLevel, double denoiseSharpness, double finalSharpness) {
    NSURL *inUrl = [NSURL fileURLWithPath:inPath];
    CIImage *input = [CIImage imageWithContentsOfURL:inUrl];
    if (!input) {
        printf("FAILED to read: %s\n", [inPath UTF8String]);
        return NO;
    }
    
    CGRect extent = [input extent];
    int origW = (int)extent.size.width;
    int origH = (int)extent.size.height;
    if (origW <= 0 || origH <= 0) {
        printf("FAILED (invalid dimensions): %s\n", [inPath UTF8String]);
        return NO;
    }
    
    // 1. Edge-preserving noise and artifact reduction
    CIFilter *denoise = [CIFilter filterWithName:@"CINoiseReduction"];
    [denoise setValue:input forKey:kCIInputImageKey];
    [denoise setValue:@(noiseLevel) forKey:@"inputNoiseLevel"];
    [denoise setValue:@(denoiseSharpness) forKey:@"inputSharpness"];
    CIImage *output = [denoise outputImage];
    
    // 2. Luminance sharpening to maintain fine contrast without halos
    if (finalSharpness > 0.0) {
        CIFilter *sharpen = [CIFilter filterWithName:@"CISharpenLuminance"];
        [sharpen setValue:output forKey:kCIInputImageKey];
        [sharpen setValue:@(finalSharpness) forKey:@"inputSharpness"];
        [sharpen setValue:@(1.2) forKey:@"inputRadius"];
        output = [sharpen outputImage];
    }
    
    // Render using hardware-accelerated context
    CIContext *ctx = [CIContext contextWithOptions:@{kCIContextUseSoftwareRenderer: @NO}];
    CGImageRef cgImg = [ctx createCGImage:output fromRect:extent];
    if (!cgImg) {
        printf("FAILED to render: %s\n", [inPath UTF8String]);
        return NO;
    }
    
    size_t outW = CGImageGetWidth(cgImg);
    size_t outH = CGImageGetHeight(cgImg);
    if ((int)outW != origW || (int)outH != origH) {
        printf("CRITICAL: Dimension mismatch in %s (orig %dx%d vs out %zux%zu)\n",
               [inPath UTF8String], origW, origH, outW, outH);
        CGImageRelease(cgImg);
        return NO;
    }
    
    NSString *ext = [[outPath pathExtension] lowercaseString];
    CFStringRef uti = (__bridge CFStringRef)UTTypePNG.identifier;
    NSDictionary *options = nil;
    
    if ([ext isEqualToString:@"jpg"] || [ext isEqualToString:@"jpeg"]) {
        uti = (__bridge CFStringRef)UTTypeJPEG.identifier;
        options = @{(__bridge NSString *)kCGImageDestinationLossyCompressionQuality: @(1.0)};
    } else if ([ext isEqualToString:@"webp"]) {
        uti = (__bridge CFStringRef)UTTypeWebP.identifier;
    }
    
    // Ensure parent dir exists
    [[NSFileManager defaultManager] createDirectoryAtPath:[outPath stringByDeletingLastPathComponent]
                              withIntermediateDirectories:YES attributes:nil error:nil];
    
    NSURL *outUrl = [NSURL fileURLWithPath:outPath];
    CGImageDestinationRef dest = CGImageDestinationCreateWithURL((__bridge CFURLRef)outUrl, uti, 1, NULL);
    if (!dest) {
        printf("FAILED to create dest: %s\n", [outPath UTF8String]);
        CGImageRelease(cgImg);
        return NO;
    }
    
    CGImageDestinationAddImage(dest, cgImg, (__bridge CFDictionaryRef)options);
    BOOL ok = CGImageDestinationFinalize(dest);
    CFRelease(dest);
    CGImageRelease(cgImg);
    
    if (ok) {
        printf("OK: %-40s -> %-40s [%dx%d]\n",
               [[inPath lastPathComponent] UTF8String],
               [[outPath lastPathComponent] UTF8String],
               origW, origH);
    } else {
        printf("FAILED to finalize: %s\n", [outPath UTF8String]);
    }
    return ok;
}

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        if (argc < 3) {
            printf("Usage: batch_denoise <input> <output> [noiseLevel] [denoiseSharpness] [finalSharpness]\n");
            return 1;
        }
        NSString *inPath = [NSString stringWithUTF8String:argv[1]];
        NSString *outPath = [NSString stringWithUTF8String:argv[2]];
        double noiseLevel = (argc > 3) ? atof(argv[3]) : 0.035;
        double denoiseSharpness = (argc > 4) ? atof(argv[4]) : 0.55;
        double finalSharpness = (argc > 5) ? atof(argv[5]) : 0.35;
        
        BOOL success = processImageFile(inPath, outPath, noiseLevel, denoiseSharpness, finalSharpness);
        return success ? 0 : 1;
    }
}
