#import <Foundation/Foundation.h>
#import <ImageIO/ImageIO.h>
#import <stdio.h>

int main() {
    @autoreleasepool {
        CFArrayRef types = CGImageDestinationCopyTypeIdentifiers();
        for (CFIndex i = 0; i < CFArrayGetCount(types); i++) {
            CFStringRef uti = (CFStringRef)CFArrayGetValueAtIndex(types, i);
            printf("%s\n", [(__bridge NSString *)uti UTF8String]);
        }
        CFRelease(types);
    }
    return 0;
}
