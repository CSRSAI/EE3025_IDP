#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct
{
	double Real; 
	double Imag;
} complex;

void FFT(complex *X, int n)
{
	if(n <= 1) return;
	
	//Arrays for Odd and Even halves
	complex *X_odd = (complex *) malloc(n/2 * sizeof(complex));
	complex *X_even = (complex *) malloc(n/2 * sizeof(complex));
	
	for(int i = 0; i < n/2; i++) 
	{
		X_even[i] = X[2*i];
		X_odd[i] = X[2*i+1];
	}
	
	//Recursive Calls
	FFT(X_even, n/2);	 	
	FFT(X_odd, n/2);		
	
	//FFT computation
	for(int i = 0; i < n/2; i++) 
	{
		double cosine = cos(2*M_PI*i/n);
		double sine = sin(2*M_PI*i/n);
		
		complex z;
		
		z.Real = cosine * X_odd[i].Real + sine * X_odd[i].Imag;	
		z.Imag = cosine * X_odd[i].Imag - sine * X_odd[i].Real;	
		
		X[i].Real = X_even[i].Real + z.Real;
		X[i].Imag = X_even[i].Imag + z.Imag;
		
		X[i+n/2].Real = X_even[i].Real - z.Real;
		X[i+n/2].Imag = X_even[i].Imag - z.Imag;
	}
	
	free(X_odd);
	free(X_even);
}

int main()
{	
	int n = 8;  
	double x[] = {1,2,3,4,2,1,0,0};
	
	complex *X = (complex *) malloc(n * sizeof(complex));
	
	for(int i = 0; i < n; i++) 
	{
		X[i].Real = x[i];
		X[i].Imag = 0;
	}
	FFT(X, n);
	
	for(int i = 0; i < n; i++) 
		printf("(%.5lf, %.5lf)\n", X[i].Real, X[i].Imag);
}