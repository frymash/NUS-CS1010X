# 1. Don't trust all the past year papers' solutions
# 2. Have a good night sleep tomorrow - what you need is a clear mind.
# 3. Don't print all your lecture notes, pass year papers, ....
# 4. Do a good summary of what you have learned with < 10 pages (you actually can bring 1000 pages)
#     (but, we only accept answer written on the answer sheets)
#      (and you will be returning all the given pages to us: 9 pages of answer sheets (one box is an optional
#         one -- that means, you are supposed to answer 8 pages), and 11 pages of question paper (there are
#         also boxes in there that you can use as draft....but, please answer in the answer sheets). 
#       please check before you start the test that you have the needed pages.
#
#     ... whatever font size you want
# 5. Try out all recitations done, and all tutorial done for sure.
# 6. As for past year papers, do try out April 4, 2020, and xx June 2020 (Final exam)
#     These 2 papers were set by me.
# 7. Don't panic during the test.
#     .... questions are not set in the order of difficulties....
#     .... you should move on if you see the question is too dirty/messy
#      .... there are indeed short and sweet questions around for you to collect points
# 8. To look through pass mission/sidequest (these are a bit difficult to be like in midterm)
#     (but you do have a point that you should do this for the Practical Exam)
# 9. April 4, 2020, Q4 ....this style is gone....no more there.
#     Q1...."stupid question"....for you to collect 1 mark
#     Q2 ....is our usual tracing
#     Q3.... iteration vs recursion, time and space complexity
#     Q4 ....HOF
# 10. You learn from the past, and I have to learn from the past too....that means, we have to be innovative.
#     ... innovative: ... combine things together ...(e.g. prefix sum in a different form)
#     ...
# 11. For tracing, you need to use various form of pictures/tables/stack to keep track of the calling(stack),
#     the change in value (table), and the movement of statements (pictures)...remember the correct scoping
# 12. Some tips that i may have drop to you during the recitations....(i don't like to set anything got to
#     do with the "system implementation" -- but you may see some of these and they are actually explanatable.
#   So, i have them in the midterm (accidentally).
# 13. Please check the post in the forum about space complexity....(1. we don't count the input size as part
#    of the space complexity...count auxiliary/extra space you need
# 14. Python is a "strange" because of "tuple" ....tuple is immutable - so, some of the time is actually
#     unnecessary in other languages (actually, i meant in other operations within Python too).
#     So, only knowing the operations and the data structures you use, then I can answer the time/space
#     complexity. (e.g. switch tuple with list....then, the whole thing just changes) 
# 15. Learning points:
#   .... functional abstraction....how to write Python codes (...if, for, while, range, continue, break, ...)
#           (we have 2 ways: iteration (for, while) vs recursion (calling yourself/base case, smaller case, carrying baggage)
#
#   ..... data abstraction.....this is got to do with use of tuple....
#   ..... applications/data+function: .... to solve problem ( how fast/time, how costly/space)
#   ......       .... "pattern" to solving problem: paradigms (e.g. Dynamic programming, memorization, ....)
#   ...the rest is just knowing what tools (picture? tables? stacks?...) to use.
#   .... and be very careful with the details....you should know now that switching between 2 statements
#         (the order is important)
#         can make LOTS LOTS OF difference.
# 16. You are allowed to use whatever you have unless it is stated that you cannot. But, it means that
#     you are responsible for it to be used correctly .....any small mistake in the use will not be accepted.
#      (In marking, whenever we ourselves are in doubt, we have to try your code in IDLE...)
# 17. Recursion: base case(s), smaller case, and carrying the baggage...
#  (ACTUALLY, I have put in effort to print horizontal line for you to write legibly)
# 18. KNOW THE MEANING OF THE PROGRAM so that you can then write the corresponding iteration (vs recursion) version
#    .... how do i know the meaning of a program?
#    ...  simple: try out some simple examples/numbers to trace the program
# 19. You have see what the question ask...if the question does not state the "most efficient" way...then you do whatever you want
#      if the question asks for a specific time/space complexity, then you have to comply
#       in the past runs of this course, the professor did not feel that efficiency should be an important issue here
#       but, for me, since you already know time/space complexity, you can't stop me from asking "efficient" way of doing things
# 20. Your result will be released in Luminus ...this is the system that you usually should be using for ALL NUS courses.
#     (this course uses coursemology.) .... www.luminus.nus.edu.sg -- use your nusid with the same passwd to log in. 
# 21. There are "special"/specific details that I need from your answer....please tell me everything that you observe....
# 22. Any mistake you wrote will negate whatever you wrote correctly...(I will choose the wrong one for you)
# there are 9 pages - but you only answer to 8 pages because there is a question with 3 boxes, but you should only answer
# to 2 boxes. Should you answer to all 3 boxes, we will mark the first boxes ONLY.
# "method marks"...some working - yap, i think i can give some consolation mark for effort....
#
# False or True....True...for me, i will take the False first.
# " " or without is fine for me.....

f = lambda f, g: (f, (g))
g = lambda g: g(g, g)

# do it step by step
# g(f) .... f(f,f)....(f,(f))....( lambda f,g:(f,(g)), (f) )
# lambda f,g: (f,(g)) (4,2)
# (4,(2))....(4, 2)





