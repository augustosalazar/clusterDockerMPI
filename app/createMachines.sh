#!/bin/bash
rm -rf machines && rm -rf tempMachine && sed -e 's/#.*//' -e 's/[[:blank:]]*$//' -e '/^$/d' -e '/^f/d' -e '/^:/d' -e '/^127/d' /etc/hosts | awk '{print $1,"slots=2 max-slots=2"}' >> tempMachine && sort -u tempMachine > machines
