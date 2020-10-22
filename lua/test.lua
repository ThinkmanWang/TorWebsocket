

function func1()
    return 1500/350, 1500%350
end

a, b = func1()
print(a)
print(b)

print(string.byte("1"))

print(string.sub("Hello World", 1,5))

function printASC(szTxt)

    for i = 1, #szTxt do
        szChar = string.sub(szTxt, i,i)
        print(string.byte(szChar))
    end
end

printASC("HELLO")