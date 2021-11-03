#!/usr/bin/env ruby
# Matches hbttn - hbtttttn

puts ARGV[0].scan(/hbt{2,5}n/).join
