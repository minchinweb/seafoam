---
title: Checkbox Test
date: 2024-01-31 21:42:00-0700
modified: 2025-06-14 18:57:15-0600
tags:
    - test
    - markdown
    - checkboxes
---

This is a test page to make sure "fancy" checkboxes render, the colours look
good, and that the align well when imbedded in other lists.

Likely requires `minchin.pelican.readers.commonmark` and
`minchin.md-it.fancy-tasklists`.

- [ ] `[ ]` to-do (open item)
- [/] `[/]` incomplete / half-done
- [x] `[x]` done (todo item)
- [X] `[X]` (big) done
- [-] `[-]` canceled / dropped
- [>] `[>]` forwarded
- [<] `[<]` scheduling
- [?] `[?]` question
- [!] `[!]` important
- [*] `[*]` star <!-- *] -->
- ["] `["]` quote
- [l] `[l]` location
- [L] `[L]` (big) location
- [b] `[b]` bookmark
- [i] `[i]` information / idea
- [S] `[S]` savings
- [I] `[I]` (big) idea
- [p] `[p]` pros / paraphrase
- [P] `[P]` (big) pro
- [c] `[c]` cons /choice
- [C] `[C]` (big) con
- [f] `[f]` fire / clue / find
- [k] `[k]` key
- [w] `[w]` win
- [u] `[u]` up
- [d] `[d]` down / doing
- [n] `[n]` note
- [N] `[N]` (big) note
- [@] `[@]` delegated / ongoing / character / person
- [D] `[D]` date
- [o] `[o]` event (BuJo)
- [+] `[+]` add
- [R] `[R]` research
- [B] `[B]` brainstorm
- [Q] `[Q]` quote
- [E] `[E]` example
- [A] `[A]` answer
- [r] `[r]` reward
- [T] `[T]` time
- [t] `[t]` talk
- [O] `[O]` outline / plot
- [~] `[~]` conflict
- [W] `[W]` world
- [F] `[F]` Foreshadow
- [H] `[H]` favorite / health
- [&] `[&]` symbolism
- [s] `[s]` secret
- [e] `[e]` energy
- [🚿] `[🚿]` shower
- [🦷] `[🦷]` tooth / dental
- [⛪] `[⛪]` church
- [📕] `[📕]` Book
- [🏠] `[🏠]` House
- [📺] `[📺]` TV (Show)
- [📽️] `[📽️]` Film / Movie -- **UTF-16**, not working
- [🎥] `[🎥]` Film / Movie
- [🎬] `[🎬]` Film / Movie
- [📽] `[📽]` Film / Movie
- [🎞] `[🎞]` Film / Movie
- [🎦] `[🎦]` Film / Movie
- [🚶‍♀️] `[🚶‍♀️]` Walking -- **UTF-16**, not working
- [🚶‍♂️] `[🚶‍♂️]` Walking -- **UTF-16**, not working
- [🏊‍♀️] `[🏊‍♀️]` Swimming -- **UTF-16**, not working
- [🏊‍♂️] `[🏊‍♂️]` Swimming -- **UTF-16**, not working
- [🎲] `[🎲]` Dice / Play

---

- Level 1
- [x] Level 1
- Level 1
    - Level 2
        - Level 3
- [x] Level 1
    - [x] Level 2
        - [x] Level 3

---

- [x] done with a long block of text. Second line should be a hanging indent. -- Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

---

- Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

    - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

        - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

---

- [x] Level 1 -- Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

  Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
- More Level 1
    - [x] Level 2 -- Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

      Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

      Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
        - [x] Level 3  -- Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

---

- [*] base list
    - sub-list should indent as expected under a tasklist, without this list
      also containing a tasklist. List marker should be visible, and not hidden
      under the item text.
        - and this sub-list too!
