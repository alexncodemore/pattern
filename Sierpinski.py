n=16
y=n-1  
while y>=0:
    print(" "*y,end="")
    x=0
    while(x+y<n):
        if (x&y)!=0 :
            print(" ",end=" ")
        else:
            print("*",end=" ")
        x+=1
    print()
    y-=1
'''
               * 
              * * 
             *   * 
            * * * * 
           *       * 
          * *     * * 
         *   *   *   * 
        * * * * * * * * 
       *               * 
      * *             * * 
     *   *           *   * 
    * * * *         * * * * 
   *       *       *       * 
  * *     * *     * *     * * 
 *   *   *   *   *   *   *   * 
* * * * * * * * * * * * * * * * 
'''

