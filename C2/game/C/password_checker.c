#include <string.h>

#if defined(_MSC_VER)
    #define EXPORT __declspec(dllexport)
#elif defined(__GNUC__)
    #define EXPORT __attribute__((visibility("default")))
#else
    #define EXPORT
#endif

#ifdef __cplusplus
extern "C" {
#endif

const char* CORRECT_PASSWORD = "8352";


EXPORT int check_password(const char* input_password) {

    if (input_password == NULL) {
        return 0; 
    }


    if (strcmp(input_password, CORRECT_PASSWORD) == 0) {
        return 1; 
    } else {
        return 0; 
    }
}

#ifdef __cplusplus
}
#endif