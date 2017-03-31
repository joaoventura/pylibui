%module libui
%include "typemaps.i"

%apply int * OUTPUT {int * width, int * height};

%{
    #include "ui.h"
%}

%typemap(in) int (*f)(uiWindow *w, void *data) {
    $1 = (int (*)(uiWindow *w, void *data))PyInt_AsLong($input);
 }

%inline %{
/* C-style cast */
uiControl *toUIControlPointer(void *f) {
   return (uiControl *) f;
}

%}

%include "ui.h"
