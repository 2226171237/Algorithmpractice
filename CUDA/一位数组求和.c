
/**
* 并行归约问题
*/


// 方法1：部分求和，然后再累加部分和。
// 1. 将输入数据划分到更小的数据块中
// 2. 用一个线程计算一个数据开的部分和，
// 3. 返回部分和，再cpu中计算总和。
__global__ void sumOfArrayOnGPU(float *A,float *B,int stride,int N)
{
    int t_id=blockIdx.x*blockDim.x+threadIdx.x;  // 线程id
    B[t_id]=0.;
    for(int i=t_id*stride;i<(t_id+1)*stride && i<N;i++)
    {
        B[t_id]+=A[i];
    }
}

// 方法2：相邻配对法1  线程分化严重
// 0 1 2 3 4 5 6 7 8
// 0   2   4   6   8
// 0       4       8
// 0               8
// 0
__global__ void sumOfArrayOnGPU2(float *g_idata,float *g_odata,int N)
{
    unsigned int tid=threadIdx.x;
    float *idata=g_idata+blockIdx.x*blockDim.x;  // 每个block数据的开始，数据按block的大小来划分有多少个线程就有多少个数据
    unsigned int idx=blockIdx.x*blockDim.x+tid;
    // 边界检查
    if (idx>=N)
        return;

    for (int stride=1;stride<blockDim.x;stride*=2)
    {
        if(tid%(stride*2)==0)  // 选thread
            idata[tid]+=idata[tid+stride];

        // block 内线程同步
        __syncthreads();
    }
    // 返回block 内的求和结果
    if (tid==0)
        g_odata[blockIdx.x]=idata[0];
}

// 方法1: 相邻配对法2
// 0 1 2 3 4 5 6 7 8
// 0   1   2   3   4
// 0       1       2
// 0               1
// 0
__global__ void sumOfArrayOnGPU2(float *g_idata,float *g_odata,int N)
{
    unsigned int tid=threadIdx.x;
    float * idata=g_idata+blockDim.x*blockIdx.x;
    unsigned int idx=blockDim.x*blockIdx.x+tid;
    if(tid>=N)
        return;

    for (int stride=1;stride<blockDim.x;stride*=2)
    {
        int index=2*stride*tid; // 选数据
        if (index<blockDim.x)
        {
            idata[index]+=idata[index+stride];
        }
        __syncthreads();
    }
    if (tid==0)
        g_odata[blockIdx.x]=idata[0];
}


// 方法3：交错配对法   ,这个记忆简单一些
// 0 1 2 3 4 5 6 7 8
// 0 1 2 3 4
// 0 1 3
// 0 1
// 0
__global__ void sumOfArrayOnGPU3(float *g_idata,float *g_odata,int N)
{
    unsigned int tid=threadIdx.x;
    float *idata=g_idata+blockDim.x*blockIdx.x;
    unsigned int idx=blockDim.x*blockIdx.x+tid;
    if (tid>=N)
        return;

    for(int stride=blockDim.x/2;stride>0;stride>>=1)
    {
        if(tid<stride)
        {
            idata[tid]+=idata[tid+stride];
        }

        __syncthreads();
    }

    if (tid==0)
        g_odata[blockIdx.x]=idata[0];
}


// 方法4：循环展开
// 一个block 处理两个数据块
__global__ void sumOfArrayOnGPU3(float *g_idata,float *g_odata,int N)
{
    unsigned int tid=threadIdx.x;
    unsigned int idx=2*blockIdx.x*blockDim.x+tid;
    float *idata=g_idata+2*blockDim.x*blockIdx.x;

    if(idx+blockDim.x<N)
        g_idata[idx]+=g_idata[idata+blockDim.x];
    __syncthreads();

    // 规约求和
    for(int stride=blockDim.x/2;stride>0;stride>>=1)
    {
        if (tid<stride)
        {
            idata[tid]+=idata[tid+stride];
        }
        __syncthreads();
    }

    if (tid==0)
        g_odata[blockIdx.x]=idata[0];
}

// 方法5 ： 展开线程的规约
__global__ void sumOfArrayOnGPU3(float *g_idata,float *g_odata,int N)
{
    unsigned int tid=threadIdx.x;
    unsigned int idx=2*blockIdx.x*blockDim.x+tid;
    float *idata=g_idata+2*blockDim.x*blockIdx.x;

    if(idx+blockDim.x<N)
        g_idata[idx]+=g_idata[idata+blockDim.x];
    __syncthreads();

    // 规约求和
    for(int stride=blockDim.x/2;stride>32;stride>>=1)
    {
        if (tid<stride)
        {
            idata[tid]+=idata[tid+stride];
        }
        __syncthreads();
    }

    if(tid<32)
    {
        volatile float *vmem=idata;
        vmem[tid]+=vem[tid+32];
        vmem[tid]+=vem[tid+16];
        vmem[tid]+=vem[tid+8];
        vmem[tid]+=vem[tid+4];
        vmem[tid]+=vem[tid+2];
        vmem[tid]+=vem[tid+1];
    }
    if (tid==0)
        g_odata[blockIdx.x]=idata[0];
}
