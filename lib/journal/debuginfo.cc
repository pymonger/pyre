// -*- C++ -*-
// 
// michael a.g. aïvázis
// california institute of technology
// (c) 1998-2011 all rights reserved
// 

// build system
#include <portinfo>

// packages
#include <cstdarg>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <vector>
#include <string>
#include <sstream>

// local types
#include "Device.h"
#include "Chronicler.h"
#include "Inventory.h"
#include "Index.h"
#include "Channel.h"
// diagnostics
#include "Diagnostic.h"
#include "Null.h"
#include "Debug.h"
#include "Locator.h"
#include "manipulators.h"

// access the declarations
#include "debuginfo.h"

// convenience
typedef pyre::journal::Debug debug_t;


// hit
extern "C"
int debuginfo_active(const char * channel)
{
    // get the channel state and return it
    return debug_t(channel).isActive();
}


// activate
extern "C"
void debuginfo_activate(const char * channel)
{
    // get the channel state and return it
    return debug_t(channel).activate();
}


// hit
extern "C"
void debuginfo_deactivate(const char * channel)
{
    // get the channel state and return it
    return debug_t(channel).deactivate();
}


// check
extern "C"
void debuginfo_out(const char * channel, __HERE_DECL__, const char * fmt, ...)
{
    // build a debug object
    debug_t debug(channel);

    // if the channel is active
    if (debug.isActive()) {
        // pull the varargs
        std::va_list args;
        char buffer[4096];
        va_start(args, fmt);
        std::vsprintf(buffer, fmt, args);
        va_end(args);
    
        // log the message
        debug
            << pyre::journal::Locator(__HERE_ARGS__)
            << buffer
            << pyre::journal::endl;
    }

    // all done
    return;
}


// end of file