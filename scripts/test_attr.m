#import <Foundation/Foundation.h>
#import <CoreImage/CoreImage.h>
#import <stdio.h>

int main() {
    @autoreleasepool {
        for (NSString *filterName in @[@"CINoiseReduction", @"CISharpenLuminance", @"CIUnsharpMask"]) {
            CIFilter *f = [CIFilter filterWithName:filterName];
            if (f) {
                printf("=== %s ===\n", [filterName UTF8String]);
                NSDictionary *attr = [f attributes];
                for (NSString *k in attr) {
                    printf("  %s: %s\n", [k UTF8String], [[NSString stringWithFormat:@"%@", attr[k]] UTF8String]);
                }
            }
        }
    }
    return 0;
}
