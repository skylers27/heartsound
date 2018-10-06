import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;

public class PeakDetection {
	int wave[] = new int[100000];
	int fs = 400;
	double t[] = new double[wave.length];
	int index = 0;
	for (double j = 0;j< (wave.length-1)/fs;j = j + 1/fs) {
		t[index] = j;
		index++;
	}

	double threshold = .15;
	int last = t.length;
	double lasttime = t[t.length - 1];
	//plot([0, lasttime], [threshold, threshold])
	int sample = (int)(fs/3);

	//initialize potential max value array 
	int potential[] = new int[(int)(last/sample)];
	int ctr = 0; //array counter

	//finds all potential max values above threshold in file
	for (int i = 0;i < (last-sample); i = i + sample) {
		int[] temp = Arrays.copyOfRange(wave, i, i+sample);
		int maxIndex = 0;
		int maxVal = temp[0];
	    for (int ktr = 0; ktr < temp.length; ktr++) {
	        if (temp[ktr] > maxVal) {
	            maxVal = temp[ktr];
	            maxIndex = ktr;
	        }
	    }
	    int actualVal = (wave[maxIndex+i]);
	    int actualIndex = maxIndex+i;
	    if (actualVal>threshold) {
	        potential[ctr] = index;
	        ctr = ctr + 1;
	    }
	}

	int noduplicate[] = new int[potential.length]; //length of potential max value array
	int lastpotential = 0;
	while(noDuplicate[lastpotential]!=0) {
		lastpotential++;
	}
	

	//filters out max values closer than .2 seconds together
	double timethreshold = .2;
	int thresholdmod = 4;
	int duplicate = 0;
	
	for (int k = 0; lastpotential; k++) {
	    if (k == lastpotential){
	        //plot([t(potential(i)), t(potential(i))], [-threshold*thresholdmod, threshold*thresholdmod], 'red');
	    }
	    for (int j = (k+1); j<lastpotential; j++) {
	        duplicate = 0;
	        if ((t[potential[j]]-t[potential[j]]) < timethreshold){
	            duplicate = 1;
	        }
	    }
	    if (duplicate == 0) {
	        //plot(t(potential(i)), wave(potential(i)), 'o');
	        //plot([t(potential(i)), t(potential(i))], [-threshold*thresholdmod, threshold*thresholdmod], 'red')
	        noduplicate[ctr] = potential[i];
	        ctr = ctr + 1;
	    }
	}

	int first = 1;
	last = 0;
	int prevval = -1;
	double prevt;
    double currentt;
    double nextt;
	//0 = systole; 1 = diastole
	//txts = '\leftarrow s';
	//txtd = '\leftarrow d';
	 for (i = 0; i<noduplicate.length; i++) {
	     if (i == 1) {
	         first = 0;
	     }
	     if (i == noduplicate.length) {
	         last = 1;
	         if (prevval == 1) {
	             //text(t(noduplicate(i)),wave(noduplicate(i)),txts)
	         }
	         else {
	           //text(t(noduplicate(i)),wave(noduplicate(i)),txtd)
	         }
	     }
	     if (first==0 && last==0) {
	        prevt = t[noduplicate[i-1]];
	        currentt = t[noduplicate[i]];
	        nextt = t[noduplicate[i+1]];
	     }
	        if (currentt-prevt > nextt-currentt) {//checks if systole
	           //text(t(noduplicate(i)),wave(noduplicate(i)),txts)
	           prevval = 0;
	        }

	           if (i == 1) {
	               //text(t(noduplicate(i-1)),wave(noduplicate(i-1)),txtd)
	           }
	        
	        else { //checks if diastole
	           //txt2 = '\leftarrow d';
	           //text(t(noduplicate(i)),wave(noduplicate(i)),txtd)
	           prevval = 1;  
	           if (i == 1) {
	               //txt2 = '\leftarrow s';
	               //text(t(noduplicate(i-1)),wave(noduplicate(i-1)),txts)
	           }
	        }
	 }
}


