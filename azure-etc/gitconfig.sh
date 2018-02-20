#!/usr/bin/env bash

# NOTE THIS REQUIRES AN EXTERNAL SETUP TO DEFINE
# ENVIRONMENT VARIALBES $GITEMAIL AND $GITNAME.

git config --global user.email $GITEMAIL
git config --global user.name $GITNAME
git config --global push.default simple

