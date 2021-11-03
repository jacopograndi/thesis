def hipass (samples):
    alpha = 0.5
    result = [0 for i in samples]
    result[0] = samples[0]
    for i in range(1, len(samples)):
        result[i] = alpha * (result[i - 1] + samples[i] - samples[i - 1])
    return result

impulse = [0 for i in range(0, 128)]
impulse[0] = 1
impulse[1] = 1
resp = hipass(impulse)
print(resp)
with open("hipass_impulse_response.txt", "w") as f: f.write(str(resp))

