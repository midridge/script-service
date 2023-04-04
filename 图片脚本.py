def plot_img_1(data: dict):
    import matplotlib.pyplot as plt
    import numpy as np
    from io import BytesIO
    import base64
    fig, ax = plt.subplots()
    legends = []
    
    for line in data['data']:
        ax.plot(line['x'], line['y'], '.')
        legends.append(line['legend'])
    plt.grid(True)
    ax.set_xlabel('{}/{}'.format(data['x.axis.label'], data['x.axis.unit']))
    ax.set_ylabel('{}/{}'.format(data['y.axis.label'], data['y.axis.unit']))
    plt.legend(legends)
    plt.title(data['title'])
    save_file = BytesIO()
    plt.savefig(save_file, format='png', dpi=600)
    return 'data:images/JPEG;base64,' + base64.b64encode(save_file.getvalue()).decode('utf-8')

result = plot_img_1(**kwargs)
