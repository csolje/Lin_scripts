#!/bin/bash
#HOSTDNS=`dig +short http.ingress.cms.pblgw.io | sort -n`
HOSTDNS=`dig +short $1 | grep -v '\.$' | sort -n`
for HOST in $HOSTDNS
do
    curl https://$HOST/login/index -k --header "Host: $1" -I
done

