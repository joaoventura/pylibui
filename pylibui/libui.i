%module libui
%include "typemaps.i"

%apply int * OUTPUT {int * width, int * height};
%apply double * OUTPUT {double *r, double *g, double *bl, double *a};

%{
    #include "ui.h"
%}

%typemap(in) int (*f)(uiWindow *w, void *data) {
    $1 = (int (*)(uiWindow *w, void *data))PyInt_AsLong($input);
 }
%typemap(in) void (*f)(uiWindow *w, void *data) {
    $1 = (void (*)(uiWindow *w, void *data))PyInt_AsLong($input);
 }
%typemap(in) void (*f)(uiButton *w, void *data) {
    $1 = (void (*)(uiButton *w, void *data))PyInt_AsLong($input);
 }
%typemap(in) void (*f)(uiCheckbox *w, void *data) {
    $1 = (void (*)(uiCheckbox *w, void *data))PyInt_AsLong($input);
 }
%typemap(in) void (*f)(uiEntry *w, void *data) {
    $1 = (void (*)(uiEntry *w, void *data))PyInt_AsLong($input);
 }
%typemap(in) void (*f)(uiSpinbox *w, void *data) {
    $1 = (void (*)(uiSpinbox *w, void *data))PyInt_AsLong($input);
 }
%typemap(in) void (*f)(uiSlider *w, void *data) {
    $1 = (void (*)(uiSlider *w, void *data))PyInt_AsLong($input);
 }
%typemap(in) void (*f)(uiCombobox *w, void *data) {
    $1 = (void (*)(uiCombobox *w, void *data))PyInt_AsLong($input);
 }
%typemap(in) void (*f)(uiEditableCombobox *w, void *data) {
    $1 = (void (*)(uiEditableCombobox *w, void *data))PyInt_AsLong($input);
 }
%typemap(in) void (*f)(uiRadioButtons *w, void *data) {
    $1 = (void (*)(uiRadioButtons *w, void *data))PyInt_AsLong($input);
 }
%typemap(in) void (*f)(uiMultilineEntry *w, void *data) {
    $1 = (void (*)(uiMultilineEntry *w, void *data))PyInt_AsLong($input);
 }
%typemap(in) void (*f)(uiMenuItem *sender, uiWindow *window, void *data) {
    $1 = (void (*)(uiMenuItem *sender, uiWindow *window, void *data))PyInt_AsLong($input);
 }
%typemap(in) void (*f)(uiFontButton *w, void *data) {
    $1 = (void (*)(uiFontButton *w, void *data))PyInt_AsLong($input);
 }
%typemap(in) void (*f)(uiColorButton *w, void *data) {
    $1 = (void (*)(uiColorButton *w, void *data))PyInt_AsLong($input);
 }
%typemap(in) void (*f)(void *data) {
    $1 = (void (*)(void *data))PyInt_AsLong($input);
 }
%typemap(in) int (*f)(void *data) {
    $1 = (int (*)(void *data))PyInt_AsLong($input);
 }
%typemap(in) void (*Draw)(uiAreaHandler *, uiArea *, uiAreaDrawParams *) {
	$1 = (void (*)(uiAreaHandler *, uiArea *, uiAreaDrawParams *))PyInt_AsLong($input);
 }
%typemap(in) void (*MouseEvent)(uiAreaHandler *, uiArea *, uiAreaMouseEvent *) {
	$1 = (void (*)(uiAreaHandler *, uiArea *, uiAreaMouseEvent *))PyInt_AsLong($input);
 }
%typemap(in) void (*MouseCrossed)(uiAreaHandler *, uiArea *, int left) {
	$1 = (void (*)(uiAreaHandler *, uiArea *, int left))PyInt_AsLong($input);
 }
%typemap(in) void (*DragBroken)(uiAreaHandler *, uiArea *) {
	$1 = (void (*)(uiAreaHandler *, uiArea *))PyInt_AsLong($input);
 }
%typemap(in) int (*KeyEvent)(uiAreaHandler *, uiArea *, uiAreaKeyEvent *) {
	$1 = (int (*)(uiAreaHandler *, uiArea *, uiAreaKeyEvent *))PyInt_AsLong($input);
 }


%inline %{
/* C-style cast */
uiControl *toUIControlPointer(void *f) {
   return (uiControl *) f;
}

uiArea *toUIAreaPointer(PyObject *f) {
    return (uiArea *) PyInt_AsLong(f);
}

uiAreaDrawParams *toUIAreaDrawParamsPointer(PyObject * f) {
    return (uiAreaDrawParams *) PyInt_AsLong(f);
}

uiAreaMouseEvent *toUIAreaMouseEventPointer(PyObject * f) {
    return (uiAreaMouseEvent *) PyInt_AsLong(f);
}

uiAreaKeyEvent *toUIAreaKeyEventPointer(PyObject * f) {
    return (uiAreaKeyEvent *) PyInt_AsLong(f);
}
%}

%include "ui.h"
