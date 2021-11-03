#!/usr/bin/env ruby
# Matches hbttn - hbtttttn

puts ARGV[0].scan(/hb{0,1}tn/).join
