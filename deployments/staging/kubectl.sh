#!/bin/bash -eux

set -eux

curl -s https://api.github.com/repos/kubernetes-sigs/kustomize/releases/latest | \
grep -E 'browser_download.+linux' | \
cut -d '"' -f 4 | \
xargs -r -t curl -L -o /usr/local/bin/kustomize
chmod +x /usr/local/bin/kustomize

cd deployments/staging || exit 1
mkdir -p secret
echo -n "$MACKEREL_APIKEY" > secret/MACKEREL_APIKEY
kustomize edit set image "gcr.io/${PROJECT_ID}/martian_imperial_year_table=gcr.io/${PROJECT_ID}/martian_imperial_year_table:${SHORT_SHA}"
kustomize build | \
/builder/kubectl.bash apply \
  -n staging \
  -l app=martian-imperial-year-table \
  --prune \
  -f -
