class Solution {
    List<List<Integer>> arr=new LinkedList<List<Integer>>();
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<Integer> ar=new LinkedList<Integer>();
        traversal(0,k,0,ar,n,1);
        return arr;
    }
    public void traversal(int c,int k,int s,List<Integer> ar,int n,int st){
        if(c==k && s==n){
            arr.add(new LinkedList<>(ar));
            return;
        }
        else if(c>k || s>n){
            return;
        }
        for(int i=st;i<=9;i++){
            ar.add(i);
            traversal(c+1,k,s+i,ar,n,i+1);
            ar.remove(ar.size()-1);
        }
    }
}