# frozen_string_literal: true

require 'shellwords'

# @param [String] str
# @return [String]
def escp(str)
  Shellwords.escape(str)
end

# @param [String] cmd
# @param [Integer] interval_sec
# @return Thread
def sh_loop(cmd, interval_sec = 30)
  Thread.new do
    loop do
      sh cmd
      sleep interval_sec
    end
  end
end

# @param [String] cmd
# @return Thread
def sh_stream(cmd)
  Thread.new { sh cmd }
end

# #!/bin/bash -eux
# shellcheck "$0"
# NS=martian-imperial-year-table-staging
# kubectl get no
# kubectl top no
# kubectl -n "$NS" get all,cm,ing,secrets
# kubectl -n "$NS" top po
# stern -n "$NS" --tail 1 martian-imperial-year-table &
# kubectl -n "$NS" get ev -o wide -w | tail -f &
# stern -n cert-manager --tail 1 cert-manager &
# stern -n ingress-nginx --tail 1 ingress-nginx &
#
# function handle_sigint() {
#     kill %1
#     kill %2
#     kill %3
#     kill %4
#     exit 0
# }
# trap handle_sigint SIGINT
# set +x
# while true ; do
#   sleep 60
# done
#
# @param [String] k8s_ns Kubernetes namespace.
def top_k8s(k8s_ns)
  threads = [
    sh_loop('kubectl get no && kubectl top no'),
    sh_loop("kubectl -n #{escp(k8s_ns)} get all,cm,ing,secret && kubectl -n #{escp(k8s_ns)} top po"),
    sh_stream("stern -n #{escp(k8s_ns)} --tail 1 martian-imperial-year-table"),
    sh_stream("kubectl -n #{escp(k8s_ns)} get ev -o wide -w | tail -f"),
    sh_stream('stern -n cert-manager --tail 1 cert-manager'),
    sh_stream('stern -n ingress-nginx --tail 1 ingress-nginx')
  ]
  Signal.trap('INT') { threads.each(&:kill) }
  threads.each(&:join)
end

desc 'Format me'
task(:format) { sh 'rubocop -a Rakefile || true' }

namespace :production do
  desc 'Inspect about staging'
  task(:top) { top_k8s('martian-imperial-year-table-production') }
end

namespace :staging do
  desc 'Inspect about staging'
  task(:top) { top_k8s('martian-imperial-year-table-staging') }
end
