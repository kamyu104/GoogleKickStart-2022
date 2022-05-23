# [GoogleKickStart 2022](https://codingcompetitions.withgoogle.com/kickstart/archive/2022) ![Language](https://img.shields.io/badge/language-Python3-orange.svg) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE) ![Progress](https://img.shields.io/badge/progress-12%20%2F%2012-ff69b4.svg) ![Visitors](https://visitor-badge.laobi.icu/badge?page_id=kamyu104.googlekickstart.2022)

* Python3 solutions of Google Kick Start 2022. Solution begins with `*` means it will get TLE in the largest data set.
* Total computation amount > `10^8` is not friendly for Python3 to solve in 5 ~ 15 seconds.
* A problem was marked as `Very Hard` means that it was an unsolved one during the contest and may not be that difficult.

## Rounds

* [Kick Start 2021](https://github.com/kamyu104/GoogleKickStart-2021)
* [Round A](https://github.com/kamyu104/GoogleKickStart-2022#round-a)
* [Round B](https://github.com/kamyu104/GoogleKickStart-2022#round-b)
* [Round C](https://github.com/kamyu104/GoogleKickStart-2022#round-c)

## Round A
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Speed Typing](https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e7021)| [Python3](./Round%20A/speed_typing.py3)| _O(\|P\|)_ | _O(1)_ | Easy | | String |
|B| [Challenge Nine](https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e7997)| [Python3](./Round%20A/challenge_nine.py3) | _O(logN)_ | _O(logN)_ | Easy | | Math, Greedy |
|C| [Palindrome Free Strings](https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e762e)| [Python3](./Round%20A/palindrome_free_strings.py3) [Python3](./Round%20A/palindrome_free_strings2.py3) | _O(N)_ | _O(1)_ | Medium | | Backtracking, DP |
|D| [Interesting Integers](https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e73ea)| [Python3](./Round%20A/interesting_integers.py3) [Python3](./Round%20A/interesting_integers2.py3) | precompute: _O(2835 * log(MAX_B)^2)_<br>runtime: _O(9 * (logB)^2)_ | _O(2835 * log(MAX_B)^2)_ | Hard | | Counting, Memoization |

## Round B
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Infinity Area](https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74/0000000000acf079)| [Python3](./Round%20B/infinity_area.py3)| _O(logR)_ | _O(1)_ | Easy | | Math |
|B| [Palindromic Factors](https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74/0000000000acee89)| [Python3](./Round%20B/palindromic_factors.py3) | _O(sqrt(A) * logA)_ | _O(1)_ | Easy | | Math, String |
|C| [Unlock the Padlock](https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74/0000000000acef55)| [Python3](./Round%20B/unlock_the_padlock.py3) | _O(N^2)_ | _O(N^2)_ | Medium | | Memoization |
|D| [Hamiltonian Tour](https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74/0000000000acf318)| [Python3](./Round%20B/hamiltonian_tour.py3) [PyPy3](./Round%20B/hamiltonian_tour2.py3) [Python3](./Round%20B/hamiltonian_tour3.py3) | _O(R * C)_ | _O(R * C)_ | Hard | | DFS, Constructive Algorithms, BFS, Spanning Tree, Wall Follower |

## Round C
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [New Password](https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb4d1/0000000000b20f15)| [Python3](./Round%20C/new_password.py3)| _O(N)_ | _O(1)_ | Easy | | String |
|B| [Range Partition](https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb4d1/0000000000b20deb)| [Python3](./Round%20C/range_partition.py3) | _O(N)_ | _O(1)_ | Easy | | Math, Greedy |
|C| [Ants on a Stick](https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb4d1/0000000000b209bc)| [Python3](./Round%20C/ants_on_a_stick.py3) [Python3](./Round%20C/ants_on_a_stick2.py3) | _O(NlogN)_ | _O(N)_ | Medium | | Sort, Deque |
|D| [Palindromic Deletions](https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb4d1/0000000000b20d16)| [PyPy3](./Round%20C/palindromic_deletions.py3) | _O(N^3)_ | _O(N^2)_ | Hard | | Math, Expected Value, Combinatorics, DP, Inclusion-Exclusion Principle |
