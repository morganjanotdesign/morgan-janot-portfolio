#import <Foundation/Foundation.h>
#import <CoreImage/CoreImage.h>
#import <CoreGraphics/CoreGraphics.h>
#import <ImageIO/ImageIO.h>
#import <UniformTypeIdentifiers/UniformTypeIdentifiers.h>

void compositeOnDark(NSString *inPath, NSString *outPath) {
    NSURL *url = [NSURL fileURLWithPath:inPath];
    CIImage *img = [CIImage imageWithContentsOfURL:url];
    
    // Create dark background (#0e0e10 -> r:14/255, g:14/255, b:16/255)
    CIImage *dark = [CIImage imageWithColor:[CIColor colorWithRed:14.0/255.0 green:14.0/255.0 blue:16.0/255.0 alpha:1.0]];
    dark = [dark imageByCroppingToRect:[img extent]];
    
    // Composite over dark
    CIImage *comp = [img imageByCompositingOverImage:dark];
    
    CIContext *ctx = [CIContext contextWithOptions:nil];
    CGImageRef cgImg = [ctx createCGImage:comp fromRect:[img extent]];
    
    NSURL *outUrl = [NSURL fileURLWithPath:outPath];
    CGImageDestinationRef dest = CGImageDestinationCreateWithURL((__bridge CFURLRef)outUrl, (__bridge CFStringRef)UTTypeJPEG.identifier, 1, NULL);
    CGImageDestinationAddImage(dest, cgImg, NULL);
    CGImageDestinationFinalize(dest);
    CFRelease(dest);
    CGImageRelease(cgImg);
}

int main() {
    @autoreleasepool {
        compositeOnDark(@"speaker_01_front.png", @"test_on_dark_1.jpg");
        compositeOnDark(@"speaker_02_threequarter.png", @"test_on_dark_2.jpg");
        compositeOnDark(@"speaker_03_back.png", @"test_on_dark_3.jpg");
        compositeOnDark(@"speaker_04_macro.png", @"test_on_dark_4.jpg");
        NSLog(@"Composited all 4 onto dark background!");
    }
    return 0;
}
