class MetricCalculator:
    def __init__(self):
        self.results = []
    
    def calculate_mean(self, data):
        try:
            if len(data)==0: return 0   #增加空列表判定
        except TypeError:
            print("非列表类型")
            return None
        try:
            return sum(data) / len(data)
        except TypeError:
            print("列表含有非数字类型")
    
    def calculate_accuracy(self, y_true, y_pred):
        try:
            if len(y_true)==0:
                return 1 if len(y_pred)==0 else 0
        except TypeError:
            print("非列表类型")
            return None
        # correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
        correct = []
        i = 0
        j = 0
        while i<len(y_true) and j<len(y_pred):
            correct.append(1 if y_true[i]==y_pred[j] else 0)
            i+=1; j+=1
        if i<len(y_true):
            correct.append(0)
            i += 1
        if j<len(y_pred):
            correct.append(0)
            j += 1
        #return correct / len(y_true)
        return sum(correct) / len(correct)
    
    def add_metric(self, name, value):
        self.results.append((name, value))
    
    def get_results(self):
        return self.results
