# 0x10. HTTPS SSL



### What I should learn:
* What is HTTPS SSL 2 main roles
* What is the purpose encrypting traffic
* What SSL termination means

### Requirements:
* ubuntu 14.04 LTS
* pass Shellcheck

## Tasks
* 0-https_abc => this file answers the following questions:
1) What is HTTPS? 2) Why do you need HTTPS? 3) You want to setup HTTPS on your website, where shall you place the certificate?

* 1-world_wide_web => Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01)

* 2-haproxy_ssl_termination => “Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to the next hope.