#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Document Parser module for Multivio"""

__author__ = "Johnny Mariethoz <Johnny.Mariethoz@rero.ch>"
__version__ = "0.0.0"
__copyright__ = "Copyright (c) 2009 Rero, Johnny Mariethoz"
__license__ = "Internal Use Only"


#---------------------------- Modules ---------------------------------------

# import of standard modules
import sys
import os
from optparse import OptionParser
import pyPdf
if sys.version_info < (2, 6):
    import simplejson as json
else:
    import json
import re

# local modules
import logger
import logging
from mvo_config import MVOConfig

#----------------------------------- Exceptions --------------------------------

class ParserError:
    """Base class for errors in the DocumentParser packages."""
    class InvalidDocument(Exception):
        """The document is not valid."""
        pass
    class InvalidParameters(Exception):
        """The type of the input parameters is not correct."""
        pass

#----------------------------------- Classes -----------------------------------

#_______________________________________________________________________________
class DocumentParser(object):
    """Base class to parse document"""
#_______________________________________________________________________________
    def __init__(self, file_stream):
        self._file_stream = file_stream
        self.logger = logging.getLogger(MVOConfig.Logger.name + "."
                        + self.__class__.__name__) 
        if self._check() is not True:
            raise ParserError.InvalidDocument("The file is invalid. (is it" \
                    "corrupted?)")

    def _check(self):
        """Check if the document is valid."""
        return True

    def getMetaData(self):
        """Get the Metadata of the document.
        Such as title, author, etc.
        """
        return None

    def getLogicalStructure(self):
        """Get the logical structure of the document.
        Such as Table of Contents.
        """
        return None

    def getPhysicalStructure(self):
        """Get the physical structure of the document.
        Such as list of images.
        """
        return None

