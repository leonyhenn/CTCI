package Ch1;

public class StringBuilderExample {
  // if we assume in words, each string has same length of x, and words.length == n, then runtime will be (xn^2);
  public String joinWords(String[] words){
    String sentence = "";
    // n iterations
    for(String w: words){
      // in each iteration, (sentence + w).length is copied to sentence, due to sentence is a string which is backed by a char array in Java,
      // Since array is immutable, each time on copy/paste, an entirely new String is created.
      sentence = sentence + w;
    }
    // if we sums up, total would come to x * (x + 2x + 3x + ... + nx ) = x * n(n + 1) / 2 = xn^2
    return sentence;
  }

  // by using string builder can prevent joinWords's high runtime problem. 
  public String usingStringBuilder(String[] words){
    
    StringBuilder sb = new StringBuilder();
    // It creates a resizable array of all strings, copying them back to a string only when necessary.
    for (String w: words){
      sb.append(w);
    }
    return sb.toString();
  }

  public static void main(String[] args){
    StringBuilderExample sbe = new StringBuilderExample();
    String result = "";
    String[] joinWordsArgs = {"123","abc"};
    
    // ---joinWords---
    // result = sbe.joinWords(joinWordsArgs);
    // System.out.println(result);

    // ---StringBuilder---
    result = sbe.usingStringBuilder(joinWordsArgs);
    System.out.println(result);
  }
}