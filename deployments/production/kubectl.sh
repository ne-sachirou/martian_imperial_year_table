#!/bin/bash -eux

set -eux

# https://github.com/kubernetes-sigs/kustomize/blob/master/docs/INSTALL.md
curl -s https://api.github.com/repos/kubernetes-sigs/kustomize/releases |\
  grep browser_download |\
  grep linux |\
  cut -d '"' -f 4 |\
  grep /kustomize/v |\
  sort | tail -n 1 |\
  xargs -t curl -O -L
tar vxzf ./kustomize_v*_linux_amd64.tar.gz
mv kustomize /usr/local/bin

cd deployments/production || exit 1
mkdir -p secret
echo -n "$MACKEREL_APIKEY" > secret/MACKEREL_APIKEY
kustomize edit set image "gcr.io/${PROJECT_ID}/martian_imperial_year_table=gcr.io/${PROJECT_ID}/martian_imperial_year_table:${SHORT_SHA}"
kustomize build | \
/builder/kubectl.bash apply \
  -n default \
  -l app=martian-imperial-year-table \
  --prune \
  -f -
