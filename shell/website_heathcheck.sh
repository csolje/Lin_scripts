#!/bin/bash
#HOSTDNS=`dig +short http.ingress.cms.pblgw.io | sort -n`
while read line; do curl -I -k -s https://$line/login/index --header "Host: $1"; done < <(dig +short $1 | grep -v '\.$' | sort -n)  | grep -E "HTTP|X-Nginx"
#HOSTDNS=`dig +short $1 | grep -v '\.$' | sort -n`
#for HOST in $HOSTDNS
#do
#    curl https://$HOST/login/index -k --header "Host: $1" -I
#done

