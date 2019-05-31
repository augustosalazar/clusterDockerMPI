#!/bin/bash
sed -e 's/#.*//' -e 's/[[:blank:]]*$//' -e '/^$/d' -e '/^f/d' -e '/^:/d' /etc/hosts | awk '{print $1}' >> machines

sort -u machines