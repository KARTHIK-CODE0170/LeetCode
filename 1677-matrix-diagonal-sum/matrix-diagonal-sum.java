class Solution {
    public int diagonalSum(int[][] mat) {
        int i = 0, j = 0,sum =0;
        for(i = 0; i < mat.length; i++)
        {
            for(j = 0; j < mat[i].length; j++)
            {
                if(i == j || i+j == mat.length -1)
                sum += mat[i][j];
            }
        }
        return sum;

    }
}