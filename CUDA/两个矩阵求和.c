
// 两个矩阵求和
__global__ void  addTwoMatrixOnGPU(float *A,float *B,float *C,int rows,int cols)
{
    int t_x=blockIdx.x*blockDim.x+threadIdx.x;
    int t_y=blockIdx.y*blockDim.y+threadIdx.y;
    int idx=t_y*cols+t_x;
    if (t_x<cols  && t_y<rows)
        C[idx]=A[idx]+B[idx];
}
