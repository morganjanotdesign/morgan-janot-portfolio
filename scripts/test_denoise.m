#import <Foundation/Foundation.h>
#import <CoreImage/CoreImage.h>
#import <ImageIO/ImageIO.h>
#import <UniformTypeIdentifiers/UniformTypeIdentifiers.h>
#import <stdio.h>

void processImage(NSString *inPath, NSString *outPath, double noiseLevel, double sharpness) {
    NSURL *inUrl = [NSURL fileURLWithPath:inPath];
    CIImage *input = [CIImage imageWithContentsOfURL:inUrl];
    if (!input) {
        printf("Failed to load: %s\n", [inPath UTF8String]);
        return;
    }
    
    CGRect extent = [input extent];
    printf("Processing %s: %.0fx%.0f\n", [[inPath lastPathComponent] UTF8String], extent.size.width, extent.size.height);
    
    CIFilter *denoise = [CIFilter filterWithName:@"CINoiseReduction"];
    [denoise setValue:input forKey:kCIInputImageKey];
    [denoise setValue:@(noiseLevel) forKey:@"inputNoiseLevel"];
    [denoise setValue:@(sharpness) forKey:@"inputSharpness"];
    
    CIImage *output = [denoise outputImage];
    
    CIContext *ctx = [CIContext contextWithOptions:@{kCIContextUseSoftwareRenderer: @NO}];
    CGImageRef cgImg = [ctx createCGImage:output fromRect:extent];
    
    NSURL *outUrl = [NSURL fileURLWithPath:outPath];
    CGImageDestinationRef dest = CGImageDestinationCreateWithURL((__bridge CFURLRef)outUrl, (__bridge CFStringRef)UTTypePNG.identifier, 1, NULL);
    CGImageDestinationAddImage(dest, cgImg, NULL);
    CGImageDestinationFinalize(dest);
    
    CFRelease(dest);
    CGImageRelease(cgImg);
    printf("Saved: %s (%.0fx%.0f)\n", [outPath UTF8String], extent.size.width, extent.size.height);
}

int main() {
    @autoreleasepool {
        processImage(
            @"/Users/morganjanot/.gemini/antigravity/brain/04838ef3-4249-4209-97cb-1440ffec4bcd/.user_uploaded/media_1790804190821.png",
            @"/Users/morganjanot/.gemini/antigravity/scratch/test_denoise_0821.png",
            0.05, 0.6
        );
        processImage(
            @"/Users/morganjanot/.gemini/antigravity/brain/04838ef3-4249-4209-97cb-1440ffec4bcd/.user_uploaded/media_1790804190785.png",
            @"/Users/morganjanot/.gemini/antigravity/scratch/test_denoise_0785.png",
            0.04, 0.6
        );
    }
    return 0;
}
