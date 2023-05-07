**1.** You are a lead engineer at **Stark Industries** working on robotics special projects. You stumble upon the old schematics of the Iron Man suit and decide to take on an ambitious project. As a savvy engineer, you realize the potential of upgrading the exoskeleton to help people walk after a neurological injury.

To ensure your exoskeleton is affordable and slim, you generate a new composite structure combining fiberglass, aluminum, and carbon nanotube materials. Ultimately, you need to assess the price of each material. 

**1st iteration:** You use 7 units of fiberglass, 5 units of aluminum, and 3 units of carbon nanotubes, which cost $120.

**2nd iteration:** You engineer a less wasteful process that uses 3 units of fiberglass, 2 units of aluminum, and 5 units of carbon nanotubes to produce the same amount of composite, the total cost is $70.

**3rd iteration:** You combine electrostimulation delivery, which cuts down the cost of the suit by using only 1 unit of fiberglass, 2 units of aluminum, and 1 unit of carbon nanotubes, which cost $20. 

**Which of the following represents the correct system of equations?**
- [ ] (A)

$$\begin{cases} 7a + 5f + 3c = 120 \cr 2f + 3a + 5c = 70 \cr 2c + a + f = 20 \end{cases}$$
- [ ] (B)

$$\begin{cases} 7f + 5a + 3c = 120 \cr 3f + 2a + 5c = 70 \end{cases}$$
- [x] (C)

$$\begin{cases} 7f + 5a + 3c = 120 \cr 3f + 2a + 5c = 70 \cr f + 2a + c = 20 \end{cases}$$
- [ ] (D)

$$\begin{cases} f + a + 3c = 100 \cr 3f + 2a + 5c = 20 \cr f + 5a + c = 50 \end{cases}$$

**2. Which of the following steps can you take to solve the system of equations? Select all that apply.**
- [x] Divide the first equation by 7.
- [x] Isolate one variable and substitute into the next equation to find the other variable.
- [x] Multiply the first equation by 3 and subtract it from equation 2.
- [x] Subtract the second row from the first row.
- [x] Multiply by a scalar and add the two rows. 

**3. Which of the following information can you extract from the given system of equations?**
- [ ] The weight and shape of each material.
- [x] Whether the matrix is singular or non-singular.
- [x] Row-reduced echelon form.
- [x] The rank of the matrix.
- [x] The cost of each material. 
- [x] Number of linearly (in)dependent rows and columns.

**4. Which of the following matrices represents the system of sentences in Q1 for all three iterations?**
- [ ] (A)

$$\begin{bmatrix} 7 & 5 \cr 2 & 3 \cr 1 & 2 \end{bmatrix}$$
- [x] (B)

$$\begin{bmatrix} 7 & 5 & 3 \cr 3 & 2 & 5 \cr 1 & 2 & 1 \end{bmatrix}$$
- [ ] (C)

$$\begin{bmatrix} 7 & 2 & 1 \cr 5 & 3 & 2 \cr 3 & 5 & 1 \end{bmatrix}$$
- [ ] (D)

$$\begin{bmatrix} 7 & 5 & 3 \cr 2 & 3 & 5 \end{bmatrix}$$

**5. Calculate the cost of each material by solving the system of equations.**

Hint: You can use the method of substitution, or row reducing the matrix to a simpler form. 
- [ ] fiberglass = $5, aluminum = $0, carbon nanotubes = $5
- [x] fiberglass = $15, aluminum = $0, carbon nanotubes = $5
- [ ] each material = $15
- [ ] fiberglass = $15, aluminum = $5, carbon nanotubes = $0

**6. Use the determinant to find if the matrix is singular or non-singular. Is the matrix in Row-echelon form or Reduced row-echelon form?**

$$\begin{bmatrix} 7 & 5 & 3 \cr 3 & 2 & 5 \cr 1 & 2 & 1 \end{bmatrix}$$

- [ ] 0, Singular, Reduced row-echelon form
- [ ] -30, Non-singular, Both
- [x] -34, Non-singular, Neither
- [ ] 34, Non-singular, Neither

**7. What is the rank in the above matrix?**
- [ ] 2
- [ ] 1
- [ ] 0
- [x] 3

**8.** To assist you with your design choices, your AI assistant compiles a few matrices with different combinations of materials. Since your experiments are not free, you want to try the option that gives you the highest amount of information.

Sort the matrices from the one that provides the lowest amount of information to the highest ( from the lowest rank to the highest rank). 

$$\text{a.} \begin{bmatrix} 0 & 1 & 1 \cr 2 & 4 & 2 \cr 1 & 2 & 1 \end{bmatrix} \text{, b.} \begin{bmatrix} 7.5 & 5 & 12.5 \cr 3 & 2 & 5 \cr 0 & 0 & 0 \end{bmatrix} \text{, c.} \begin{bmatrix} 7 & 5 & 3 \cr 3 & 2 & 5 \cr 1 & 2 & 1 \end{bmatrix}$$

Hint: To help you get started, determine which matrices have linearly dependent rows. You've already found the rank of the third matrix!
- [ ] c, a, b
- [ ] a, b, c
- [x] b, a, c
- [ ] b, c, a

**9. To further optimize the cost of materials, you finally reduce your number of iterations to only 2 tries, where you now obtain a 2x2 matrix with rank 1.**

**Which of the following is your matrix?**

Hint: Which of the following 2x2 matrices have rank  = 1?
- [x] (A)

$$\begin{bmatrix} 1 & 1 \cr 2 & 2 \end{bmatrix}$$
- [ ] (B)

$$\begin{bmatrix} 0 & 0 \cr 0 & 0 \end{bmatrix}$$
- [ ] (C)

$$\begin{bmatrix} 5 & 2 \cr 10 & 3 \end{bmatrix}$$
