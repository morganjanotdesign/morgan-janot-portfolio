#import <Foundation/Foundation.h>
#import <Vision/Vision.h>
#import <CoreImage/CoreImage.h>
#import <CoreGraphics/CoreGraphics.h>
#import <CoreVideo/CoreVideo.h>
#import <ImageIO/ImageIO.h>
#import <UniformTypeIdentifiers/UniformTypeIdentifiers.h>

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        if (argc < 3) {
            printf("Usage: %s <input_image> <output_image>\n", argv[0]);
            return 1;
        }
        NSString *inputPath = [NSString stringWithUTF8String:argv[1]];
        NSString *outputPath = [NSString stringWithUTF8String:argv[2]];
        
        NSURL *inputURL = [NSURL fileURLWithPath:inputPath];
        CIImage *inputCIImage = [CIImage imageWithContentsOfURL:inputURL];
        if (!inputCIImage) {
            NSLog(@"Failed to load image at %@", inputPath);
            return 1;
        }
        
        VNGenerateForegroundInstanceMaskRequest *request = [[VNGenerateForegroundInstanceMaskRequest alloc] init];
        VNImageRequestHandler *handler = [[VNImageRequestHandler alloc] initWithCIImage:inputCIImage options:@{}];
        NSError *error = nil;
        [handler performRequests:@[request] error:&error];
        if (error) {
            NSLog(@"Request failed: %@", error);
            return 1;
        }
        
        NSArray<VNInstanceMaskObservation *> *results = [request results];
        if (!results || results.count == 0) {
            NSLog(@"No subject detected");
            return 1;
        }
        
        VNInstanceMaskObservation *observation = results.firstObject;
        CVPixelBufferRef maskPixelBuffer = [observation generateMaskedImageOfInstances:observation.allInstances fromRequestHandler:handler croppedToInstancesExtent:NO error:&error];
        if (error || !maskPixelBuffer) {
            NSLog(@"Failed to generate masked image: %@", error);
            return 1;
        }
        
        CIImage *maskedImage = [CIImage imageWithCVPixelBuffer:maskPixelBuffer];
        CIContext *context = [CIContext contextWithOptions:nil];
        CGImageRef cgImage = [context createCGImage:maskedImage fromRect:[maskedImage extent]];
        
        NSURL *outputURL = [NSURL fileURLWithPath:outputPath];
        CGImageDestinationRef destination = CGImageDestinationCreateWithURL((__bridge CFURLRef)outputURL, (__bridge CFStringRef)UTTypePNG.identifier, 1, NULL);
        if (!destination) {
            NSLog(@"Failed to create image destination for %@", outputPath);
            return 1;
        }
        CGImageDestinationAddImage(destination, cgImage, NULL);
        CGImageDestinationFinalize(destination);
        CFRelease(destination);
        CGImageRelease(cgImage);
        CVPixelBufferRelease(maskPixelBuffer);
        NSLog(@"Successfully saved transparent PNG to %@", outputPath);
    }
    return 0;
}
