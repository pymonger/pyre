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
#include "Firewall.h"
#include "Locator.h"
#include "manipulators.h"

// access the declarations
#include "firewalls.h"

// convenience
typedef pyre::journal::Firewall firewall_t;


// hit
extern "C"
void firewall_hit(const char * channel, __HERE_DECL__, const char * fmt, ...)
{
    // pull the varargs
    std::va_list args;
    char buffer[4096];
    va_start(args, fmt);
    std::vsprintf(buffer, fmt, args);
    va_end(args);
    
    // create a firewall channel
    firewall_t firewall(channel);

    // log the message
    firewall
        << pyre::journal::Locator(__HERE_ARGS__)
        << buffer
        << pyre::journal::endl;

    // all done
    return;
}


// check
extern "C"
void firewall_check(const char * channel, int condition, __HERE_DECL__, const char * fmt, ...)
{
    // if {condition} is false
    if (!condition) {
        // pull the varargs
        std::va_list args;
        char buffer[4096];
        va_start(args, fmt);
        std::vsprintf(buffer, fmt, args);
        va_end(args);
    
        // create a firewall channel
        firewall_t firewall(channel);

        // log the message
        firewall
            << pyre::journal::Locator(__HERE_ARGS__)
            << buffer
            << pyre::journal::endl;
    }

    // all done
    return;
}


// end of file