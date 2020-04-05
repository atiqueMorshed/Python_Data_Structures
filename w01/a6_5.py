text = "X-DSPAM-Confidence:    0.8475";
st = text.find("0")
end = text.find("5")
print(float(text[st:end+1]))
