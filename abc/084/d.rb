require 'prime'
require 'pp'

q = gets.to_i
primes = Prime.each(100000)

primes_2017 = primes.select { |p| Prime.prime?((p + 1) / 2) }
p_reversed = primes_2017.reverse

q.times do
    l, r = gets.strip.split.map(&:to_i)
    lower = primes_2017.bsearch_index { |p| p >= l }
    upper = p_reversed.bsearch_index { |p| p <= r }
    if lower == nil || upper == nil
        puts 0
    else
        puts (primes_2017.size - upper - 1) - lower + 1
    end
end

