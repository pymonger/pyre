// -*- C++ -*-
// 
// michael a.g. aïvázis
// california institute of technology
// (c) 1998-2012 all rights reserved
// 


#include <portinfo>
#include <Python.h>
#include <gsl/gsl_vector.h>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_randist.h>

// local includes
#include "pdf.h"
#include "capsules.h"


// uniform::sample
const char * const gsl::pdf::uniform::sample__name__ = "uniform_sample";
const char * const gsl::pdf::uniform::sample__doc__ = 
    "return a sample from the uniform distribution";

PyObject * 
gsl::pdf::uniform::sample(PyObject *, PyObject * args) {
    // the arguments
    double a, b;
    PyObject * capsule;
    // unpack the argument tuple
    int status = PyArg_ParseTuple(
                                  args, "(dd)O!:uniform_sample",
                                  &a, &b, &PyCapsule_Type, &capsule);
    // bail out if something went wrong with the argument unpacking
    if (!status) return 0;
    // bail out if the capsule is not valid
    if (!PyCapsule_IsValid(capsule, gsl::rng::capsule_t)) {
        PyErr_SetString(PyExc_TypeError, "invalid rng capsule");
        return 0;
    }
    // get the rng
    gsl_rng * r = static_cast<gsl_rng *>(PyCapsule_GetPointer(capsule, gsl::rng::capsule_t));
    // sample the distribution and return the value
    return PyFloat_FromDouble(gsl_ran_flat(r, a, b));
}


// uniform::density
const char * const gsl::pdf::uniform::density__name__ = "uniform_density";
const char * const gsl::pdf::uniform::density__doc__ = "return the uniform distribution density";

PyObject * 
gsl::pdf::uniform::density(PyObject *, PyObject * args) {
    // the arguments
    double x, a, b;
    // unpack the argument tuple
    int status = PyArg_ParseTuple(args, "(dd)d:uniform_density", &a, &b, &x);
    // bail out if something went wrong with the argument unpacking
    if (!status) return 0;
    // compute the density and return the value
    return PyFloat_FromDouble(gsl_ran_flat_pdf(x, a, b));
}


// uniform::vector
const char * const gsl::pdf::uniform::vector__name__ = "uniform_vector";
const char * const gsl::pdf::uniform::vector__doc__ = "fill a vector with random values";

PyObject * 
gsl::pdf::uniform::vector(PyObject *, PyObject * args) {
    // the arguments
    double a, b;
    PyObject * rngCapsule;
    PyObject * vectorCapsule;
    // unpack the argument tuple
    int status = PyArg_ParseTuple(
                                  args, "(dd)O!O!:uniform_vector",
                                  &a, &b,
                                  &PyCapsule_Type, &rngCapsule,
                                  &PyCapsule_Type, &vectorCapsule);
    // bail out if something went wrong with the argument unpacking
    if (!status) return 0;
    // bail out if the rng capsule is not valid
    if (!PyCapsule_IsValid(rngCapsule, gsl::rng::capsule_t)) {
        PyErr_SetString(PyExc_TypeError, "invalid rng capsule");
        return 0;
    }
    // bail out if the vector capsule is not valid
    if (!PyCapsule_IsValid(vectorCapsule, gsl::vector::capsule_t)) {
        PyErr_SetString(PyExc_TypeError, "invalid vector capsule");
        return 0;
    }
    // get the rng
    gsl_rng * rng =
        static_cast<gsl_rng *>(PyCapsule_GetPointer(rngCapsule, gsl::rng::capsule_t));
    // get the vector
    gsl_vector * v = 
        static_cast<gsl_vector *>(PyCapsule_GetPointer(vectorCapsule, gsl::vector::capsule_t));
    // fill
    for (size_t i = 0; i < v->size; i++) {
        double value = gsl_ran_flat(rng, a, b);
        gsl_vector_set(v, i, value);
    }
    // return None
    Py_INCREF(Py_None);
    return Py_None;
}


// uniform::matrix
const char * const gsl::pdf::uniform::matrix__name__ = "uniform_matrix";
const char * const gsl::pdf::uniform::matrix__doc__ = "fill a matrix with random values";

PyObject * 
gsl::pdf::uniform::matrix(PyObject *, PyObject * args) {
    // the arguments
    double a, b;
    PyObject * rngCapsule;
    PyObject * matrixCapsule;
    // unpack the argument tuple
    int status = PyArg_ParseTuple(
                                  args, "(dd)O!O!:uniform_matrix",
                                  &a, &b,
                                  &PyCapsule_Type, &rngCapsule,
                                  &PyCapsule_Type, &matrixCapsule);
    // bail out if something went wrong with the argument unpacking
    if (!status) return 0;
    // bail out if the rng capsule is not valid
    if (!PyCapsule_IsValid(rngCapsule, gsl::rng::capsule_t)) {
        PyErr_SetString(PyExc_TypeError, "invalid rng capsule");
        return 0;
    }
    // bail out if the matrix capsule is not valid
    if (!PyCapsule_IsValid(matrixCapsule, gsl::matrix::capsule_t)) {
        PyErr_SetString(PyExc_TypeError, "invalid matrix capsule");
        return 0;
    }
    // get the rng
    gsl_rng * rng =
        static_cast<gsl_rng *>(PyCapsule_GetPointer(rngCapsule, gsl::rng::capsule_t));
    // get the matrix
    gsl_matrix * m = 
        static_cast<gsl_matrix *>(PyCapsule_GetPointer(matrixCapsule, gsl::matrix::capsule_t));
    // fill
    for (size_t i = 0; i < m->size1; i++) {
        for (size_t j = 0; j < m->size2; j++) {
            double value = gsl_ran_flat(rng, a, b);
            gsl_matrix_set(m, i, j, value);
        }
    }
    // return None
    Py_INCREF(Py_None);
    return Py_None;
}


// gaussian::sample
const char * const gsl::pdf::gaussian::sample__name__ = "gaussian_sample";
const char * const gsl::pdf::gaussian::sample__doc__ = 
    "return a sample from the gaussian distribution";

PyObject * 
gsl::pdf::gaussian::sample(PyObject *, PyObject * args) {
    // the arguments
    double sigma;
    PyObject * capsule;
    // unpack the argument tuple
    int status = PyArg_ParseTuple(
                                  args, "dO!:gaussian_sample",
                                  &sigma, &PyCapsule_Type, &capsule);
    // bail out if something went wrong with the argument unpacking
    if (!status) return 0;
    // bail out if the capsule is not valid
    if (!PyCapsule_IsValid(capsule, gsl::rng::capsule_t)) {
        PyErr_SetString(PyExc_TypeError, "invalid rng capsule");
        return 0;
    }
    // get the rng
    gsl_rng * r = static_cast<gsl_rng *>(PyCapsule_GetPointer(capsule, gsl::rng::capsule_t));
    // sample the distribution and return the value
    return PyFloat_FromDouble(gsl_ran_gaussian(r, sigma));
}


// gaussian::density
const char * const gsl::pdf::gaussian::density__name__ = "gaussian_density";
const char * const gsl::pdf::gaussian::density__doc__ = "return the gaussian distribution density";

PyObject * 
gsl::pdf::gaussian::density(PyObject *, PyObject * args) {
    // the arguments
    double x, sigma;
    // unpack the argument tuple
    int status = PyArg_ParseTuple(args, "dd:gaussian_density", &sigma, &x);
    // bail out if something went wrong with the argument unpacking
    if (!status) return 0;
    // compute the density and return the value
    return PyFloat_FromDouble(gsl_ran_gaussian_pdf(x, sigma));
}


// gaussian::vector
const char * const gsl::pdf::gaussian::vector__name__ = "gaussian_vector";
const char * const gsl::pdf::gaussian::vector__doc__ = "fill a vector with random values";

PyObject * 
gsl::pdf::gaussian::vector(PyObject *, PyObject * args) {
    // the arguments
    double sigma;
    PyObject * rngCapsule;
    PyObject * vectorCapsule;
    // unpack the argument tuple
    int status = PyArg_ParseTuple(
                                  args, "dO!O!:gaussian_vector",
                                  &sigma,
                                  &PyCapsule_Type, &rngCapsule,
                                  &PyCapsule_Type, &vectorCapsule);
    // bail out if something went wrong with the argument unpacking
    if (!status) return 0;
    // bail out if the rng capsule is not valid
    if (!PyCapsule_IsValid(rngCapsule, gsl::rng::capsule_t)) {
        PyErr_SetString(PyExc_TypeError, "invalid rng capsule");
        return 0;
    }
    // bail out if the vector capsule is not valid
    if (!PyCapsule_IsValid(vectorCapsule, gsl::vector::capsule_t)) {
        PyErr_SetString(PyExc_TypeError, "invalid vector capsule");
        return 0;
    }
    // get the rng
    gsl_rng * rng =
        static_cast<gsl_rng *>(PyCapsule_GetPointer(rngCapsule, gsl::rng::capsule_t));
    // get the vector
    gsl_vector * v = 
        static_cast<gsl_vector *>(PyCapsule_GetPointer(vectorCapsule, gsl::vector::capsule_t));
    // fill
    for (size_t i = 0; i < v->size; i++) {
        double value = gsl_ran_gaussian(rng, sigma);
        gsl_vector_set(v, i, value);
    }
    // return None
    Py_INCREF(Py_None);
    return Py_None;
}


// gaussian::matrix
const char * const gsl::pdf::gaussian::matrix__name__ = "gaussian_matrix";
const char * const gsl::pdf::gaussian::matrix__doc__ = "fill a matrix with random values";

PyObject * 
gsl::pdf::gaussian::matrix(PyObject *, PyObject * args) {
    // the arguments
    double sigma;
    PyObject * rngCapsule;
    PyObject * matrixCapsule;
    // unpack the argument tuple
    int status = PyArg_ParseTuple(
                                  args, "dO!O!:gaussian_matrix",
                                  &sigma,
                                  &PyCapsule_Type, &rngCapsule,
                                  &PyCapsule_Type, &matrixCapsule);
    // bail out if something went wrong with the argument unpacking
    if (!status) return 0;
    // bail out if the rng capsule is not valid
    if (!PyCapsule_IsValid(rngCapsule, gsl::rng::capsule_t)) {
        PyErr_SetString(PyExc_TypeError, "invalid rng capsule");
        return 0;
    }
    // bail out if the matrix capsule is not valid
    if (!PyCapsule_IsValid(matrixCapsule, gsl::matrix::capsule_t)) {
        PyErr_SetString(PyExc_TypeError, "invalid matrix capsule");
        return 0;
    }
    // get the rng
    gsl_rng * rng =
        static_cast<gsl_rng *>(PyCapsule_GetPointer(rngCapsule, gsl::rng::capsule_t));
    // get the matrix
    gsl_matrix * m = 
        static_cast<gsl_matrix *>(PyCapsule_GetPointer(matrixCapsule, gsl::matrix::capsule_t));
    // fill
    for (size_t i = 0; i < m->size1; i++) {
        for (size_t j = 0; j < m->size2; j++) {
            double value = gsl_ran_gaussian(rng, sigma);
            gsl_matrix_set(m, i, j, value);
        }
    }
    // return None
    Py_INCREF(Py_None);
    return Py_None;
}


// end of file