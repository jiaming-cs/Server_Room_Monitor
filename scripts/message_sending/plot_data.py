from matplotlib import pyplot as plt
from os.path import abspath, dirname

def handle_time(time):
    out = []
    for t in time:
        out.append(t.split(" ")[1])
    return out
    
def get_graph_data(time, temp, humi):
    time = handle_time(time)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(time, temp, 'r', label="Temperature")
    ax1.set_ylabel('Tempreature / F')
    ax1.set_title("Sever Room Daily Temprature and Huminity Report")
    ax1.set_xlabel("Time (h)")
    

    ax2 = ax1.twinx()  
    ax2.plot(time, humi, 'b', label="Humidity")
    ax2.set_ylabel('Huminity / %')
    fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
    plt.savefig(abspath(dirname(__file__))+"/graphs/"+"temp_humi_graph.png")
    
