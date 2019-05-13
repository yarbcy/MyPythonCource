def filter_words(st):    
     # Your code here.
    st = st.replace('  ',' ')
    st = st.replace('  ',' ')
    st = st.lower()    
    st = list(st)
    st[0] = st[0].upper()
    if st[-1] == ' ':
        st[-1] = ''
    st = str(''.join(st))
    return str(st)