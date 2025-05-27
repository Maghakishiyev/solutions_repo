# Combinatorics

## Variations without repetition

**Formula:** $V(n,r) = P(n,r) = \frac{n!}{(n-r)!}$ where we choose $r$ objects from $n$ objects and order matters.

### Solutions:

1. **From five different balls, choose two and arrange them in a specific order. How many arrangements are possible?**
   
   $V(5,2) = \frac{5!}{(5-2)!} = \frac{5!}{3!} = \frac{5 \times 4 \times 3!}{3!} = 5 \times 4 = 20$
   
   **Answer:** 20 arrangements

2. **You have four different books. Choose two and arrange them on a shelf in a specific order. How many such arrangements are there?**
   
   $V(4,2) = \frac{4!}{(4-2)!} = \frac{4!}{2!} = \frac{4 \times 3 \times 2!}{2!} = 4 \times 3 = 12$
   
   **Answer:** 12 arrangements

3. **In a competition with 10 participants, how many ways can 3 finalists be selected and arranged in order?**
   
   $V(10,3) = \frac{10!}{(10-3)!} = \frac{10!}{7!} = 10 \times 9 \times 8 = 720$
   
   **Answer:** 720 ways

4. **You have seven different keys. Choose three and arrange them in a specific order on a table. How many possible arrangements are there?**
   
   $V(7,3) = \frac{7!}{(7-3)!} = \frac{7!}{4!} = 7 \times 6 \times 5 = 210$
   
   **Answer:** 210 arrangements

5. **At school, three people are chosen as leaders, and their roles (chairperson, deputy, and treasurer) are significant. How many different arrangements can be made for 8 candidates?**
   
   $V(8,3) = \frac{8!}{(8-3)!} = \frac{8!}{5!} = 8 \times 7 \times 6 = 336$
   
   **Answer:** 336 arrangements

## Variations with repetition

**Formula:** $V_r(n,r) = n^r$ where we choose $r$ objects from $n$ objects with repetition allowed and order matters.

### Solutions:

1. **You have three different colors of paint. How many different sequences of two colors can you create if colors can repeat?**
   
   $V_r(3,2) = 3^2 = 9$
   
   **Answer:** 9 sequences

2. **The menu includes four different types of drinks. How many different two-drink combinations can you create, allowing repetition?**
   
   $V_r(4,2) = 4^2 = 16$
   
   **Answer:** 16 combinations

3. **A lock code consists of three digits, each ranging from 1 to 5. How many different codes can be created if digits can repeat?**
   
   $V_r(5,3) = 5^3 = 125$
   
   **Answer:** 125 codes

4. **In a class, you have 6 different pens. How many different combinations of two pens in a specific order can be made, allowing repetition of the same pen?**
   
   $V_r(6,2) = 6^2 = 36$
   
   **Answer:** 36 combinations

5. **A shop offers three types of candies. How many different sets of two candies can be created if you are allowed to pick the same candy multiple times?**
   
   $V_r(3,2) = 3^2 = 9$
   
   **Answer:** 9 sets

## Permutations without repetition

**Formula:** $P(n) = n!$ where we arrange all $n$ objects in order.

### Solutions:

1. **How many different three-digit numbers can be formed using the digits 1, 2, 3, 4 if no digit repeats?**
   
   $V(4,3) = \frac{4!}{(4-3)!} = \frac{4!}{1!} = 4 \times 3 \times 2 = 24$
   
   **Answer:** 24 numbers

2. **You have 5 different letters: A, B, C, D, E. How many different words can you form using all of them?**
   
   $P(5) = 5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$
   
   **Answer:** 120 words

3. **In a group of 6 people, how many different ways can they be arranged in a line?**
   
   $P(6) = 6! = 6 \times 5 \times 4 \times 3 \times 2 \times 1 = 720$
   
   **Answer:** 720 ways

4. **You have four different pictures. In how many different ways can they be hung on a wall in a row?**
   
   $P(4) = 4! = 4 \times 3 \times 2 \times 1 = 24$
   
   **Answer:** 24 ways

5. **At school, there is a contest where 7 students need to line up in a specific order. How many different arrangements are possible?**
   
   $P(7) = 7! = 5040$
   
   **Answer:** 5040 arrangements

## Permutations with repetition

**Formula:** $P(n; n_1, n_2, ..., n_k) = \frac{n!}{n_1! \times n_2! \times ... \times n_k!}$ where $n_i$ is the number of identical objects of type $i$.

### Solutions:

1. **How many different words can be formed using the letters in the word "ANNA"?**
   
   We have 4 letters: A appears 2 times, N appears 2 times
   $P(4; 2, 2) = \frac{4!}{2! \times 2!} = \frac{24}{2 \times 2} = \frac{24}{4} = 6$
   
   **Answer:** 6 words

2. **You have a box with three red balls and two green balls. How many different orders can these balls be arranged in?**
   
   We have 5 balls: 3 red (identical) and 2 green (identical)
   $P(5; 3, 2) = \frac{5!}{3! \times 2!} = \frac{120}{6 \times 2} = \frac{120}{12} = 10$
   
   **Answer:** 10 arrangements

3. **In the word "COCONUT," there are three "O"s. How many distinct words can be formed by permuting the letters of this word?**
   
   We have 7 letters: C appears 2 times, O appears 2 times, N, U, T each appear 1 time
   $P(7; 2, 2, 1, 1, 1) = \frac{7!}{2! \times 2! \times 1! \times 1! \times 1!} = \frac{5040}{2 \times 2} = \frac{5040}{4} = 1260$
   
   **Answer:** 1260 words

4. **In a group, there are 3 people named "Adam" and 2 people named "Eve." How many different arrangements of this group are possible?**
   
   We have 5 people: 3 Adams (identical) and 2 Eves (identical)
   $P(5; 3, 2) = \frac{5!}{3! \times 2!} = \frac{120}{6 \times 2} = 10$
   
   **Answer:** 10 arrangements

5. **How many different numbers can be formed using the digits: 1, 1, 2, 2, 2?**
   
   We have 5 digits: 1 appears 2 times, 2 appears 3 times
   $P(5; 2, 3) = \frac{5!}{2! \times 3!} = \frac{120}{2 \times 6} = \frac{120}{12} = 10$
   
   **Answer:** 10 numbers

## Combinations without repetition

**Formula:** $C(n,r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}$ where we choose $r$ objects from $n$ objects and order doesn't matter.

### Solutions:

1. **You have 10 books and want to choose 4, but the order of selection doesn't matter. How many possible selections are there?**
   
   $C(10,4) = \binom{10}{4} = \frac{10!}{4!(10-4)!} = \frac{10!}{4! \times 6!} = \frac{10 \times 9 \times 8 \times 7}{4 \times 3 \times 2 \times 1} = \frac{5040}{24} = 210$
   
   **Answer:** 210 selections

2. **In a class of 15 students, how many ways can you select three for a trip?**
   
   $C(15,3) = \binom{15}{3} = \frac{15!}{3!(15-3)!} = \frac{15 \times 14 \times 13}{3 \times 2 \times 1} = \frac{2730}{6} = 455$
   
   **Answer:** 455 ways

3. **From a standard 52-card deck, you choose 5 cards. How many different hands can be formed?**
   
   $C(52,5) = \binom{52}{5} = \frac{52!}{5!(52-5)!} = \frac{52 \times 51 \times 50 \times 49 \times 48}{5 \times 4 \times 3 \times 2 \times 1} = \frac{311875200}{120} = 2598960$
   
   **Answer:** 2,598,960 hands

4. **From 8 different fruits, choose 3 without considering the order. How many such selections are there?**
   
   $C(8,3) = \binom{8}{3} = \frac{8!}{3!(8-3)!} = \frac{8 \times 7 \times 6}{3 \times 2 \times 1} = \frac{336}{6} = 56$
   
   **Answer:** 56 selections

5. **A company has 20 employees. How many ways can a 5-person team be chosen?**
   
   $C(20,5) = \binom{20}{5} = \frac{20!}{5!(20-5)!} = \frac{20 \times 19 \times 18 \times 17 \times 16}{5 \times 4 \times 3 \times 2 \times 1} = \frac{1860480}{120} = 15504$
   
   **Answer:** 15,504 ways

## Combinations with repetition

**Formula:** $C_r(n,r) = \binom{n+r-1}{r} = \binom{n+r-1}{n-1}$ where we choose $r$ objects from $n$ types with repetition allowed and order doesn't matter.

### Solutions:

1. **A shop offers 4 different types of fruit. How many different sets of 3 fruits can you buy, if the same fruit can be selected multiple times?**
   
   $C_r(4,3) = \binom{4+3-1}{3} = \binom{6}{3} = \frac{6!}{3! \times 3!} = \frac{6 \times 5 \times 4}{3 \times 2 \times 1} = 20$
   
   **Answer:** 20 sets

2. **You have 5 different types of candies. How many different sets of 4 candies can you choose if candies can repeat?**
   
   $C_r(5,4) = \binom{5+4-1}{4} = \binom{8}{4} = \frac{8!}{4! \times 4!} = \frac{8 \times 7 \times 6 \times 5}{4 \times 3 \times 2 \times 1} = 70$
   
   **Answer:** 70 sets

3. **In a restaurant, there are 6 different desserts to choose from. How many different two-dessert sets can you create if you can choose the same dessert twice?**
   
   $C_r(6,2) = \binom{6+2-1}{2} = \binom{7}{2} = \frac{7!}{2! \times 5!} = \frac{7 \times 6}{2 \times 1} = 21$
   
   **Answer:** 21 sets

4. **A flower shop offers 3 different types of flowers. How many bouquets of 5 flowers can be made if flowers can repeat?**
   
   $C_r(3,5) = \binom{3+5-1}{5} = \binom{7}{5} = \binom{7}{2} = \frac{7 \times 6}{2 \times 1} = 21$
   
   **Answer:** 21 bouquets

5. **You have 7 different ice cream flavors. How many different 4-flavor combinations can you create if flavors can repeat?**
   
   $C_r(7,4) = \binom{7+4-1}{4} = \binom{10}{4} = \frac{10!}{4! \times 6!} = \frac{10 \times 9 \times 8 \times 7}{4 \times 3 \times 2 \times 1} = 210$
   
   **Answer:** 210 combinations