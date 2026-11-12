#import <Foundation/Foundation.h>
#import <CoreImage/CoreImage.h>
#import <stdio.h>

int main() {
    @autoreleasepool {
        NSArray *all = [CIFilter filterNamesInCategories:nil];
        for (NSString *name in all) {
            if ([name containsString:@"Noise"] || [name containsString:@"Sharpen"] || [name containsString:@"Bilateral"] || [name containsString:@"Median"] || [name containsString:@"Edge"]) {
                printf("%s\n", [name UTF8String]);
            }
        }
    }
    return 0;
}
