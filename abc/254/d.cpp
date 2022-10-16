#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <set>

using llint = __int128;

#define debug(var)  do{std::cout << #var << " : ";view(var);}while(0)
template<typename T> void view(T e){std::cout << e << std::endl;}
template<typename T> void view(const std::vector<T>& v){for(const auto& e : v){ std::cout << e << " "; } std::cout << std::endl;}
template<typename T> void view(const std::vector<std::vector<T> >& vv){ for(const auto& v : vv){ view(v); } }

std::ostream &operator<<(std::ostream &dest, __int128_t value) {
  std::ostream::sentry s(dest);
  if (s) {
    __uint128_t tmp = value < 0 ? -value : value;
    char buffer[128];
    char *d = std::end(buffer);
    do {
      --d;
      *d = "0123456789"[tmp % 10];
      tmp /= 10;
    } while (tmp != 0);
    if (value < 0) {
      --d;
      *d = '-';
    }
    int len = std::end(buffer) - d;
    if (dest.rdbuf()->sputn(d, len) != len) {
      dest.setstate(std::ios_base::badbit);
    }
  }
  return dest;
}

__int128 parse(std::string &s) {
  __int128 ret = 0;
  for (int i = 0; i < s.length(); i++)
    if ('0' <= s[i] && s[i] <= '9')
      ret = 10 * ret + s[i] - '0';
  return ret;
}

std::vector<std::pair<int, int>> factorize(const int N) {
    if (N == 1) {
        return std::vector<std::pair<int, int>>(); 
    } else if (N == 2) {
        return std::vector<std::pair<int, int>> {std::make_pair(2, 1)};
    } else if (N == 3) {
        return std::vector<std::pair<int, int>> {std::make_pair(3, 1)};
    }
    std::vector<std::pair<int, int>> ret;
    int k = 2;
    int n = N;
    while (k * k <= N) {
        int a = 0;
        while (n % k == 0) {
            a += 1;
            n /= k;
        }
        if (a > 0) {
            ret.push_back(std::make_pair(k, a));
        }
        k++;
    }
    if (n != 1) {
        ret.push_back(std::make_pair(n, 1));
    }
    if (ret.size() == 0) {
        ret.push_back(std::make_pair(N, 1));
    }
    return ret;
}

std::vector<llint> all_factors(const std::vector<std::pair<int, int>>& prime_factors, const int idx) {
    if (idx == prime_factors.size()) {
        return std::vector<llint> {1};
    }

    std::vector<llint> ret;

    auto pair = prime_factors[idx];
    auto p = pair.first;
    auto a = pair.second;
    auto fs = all_factors(prime_factors, idx + 1);
    for (int b = 0; b <= 2 * a; b++) {
        for (const auto& f : fs) {
            ret.push_back(std::pow(p, b) * f);
        }
    }
    return ret;
}


int main() {
    int N;
    std::cin >> N;
    // std::cout << N << std::endl;

    std::set<std::pair<llint, llint>> result;
    for (int k = 1; k <= N; k++) {
        auto prime_factors = factorize(k);
        auto afactors = all_factors(prime_factors, 0);
        for (auto& i : afactors) {
            const llint j = (k * k) / i;
            if (i <= N && j <= N) {
                result.insert(std::make_pair(i, j));
            }
        }
    }
    std::cout << result.size() << std::endl;
    return 0;
}

