const xaxis = [...Array(100).keys()];
const yaxis = [...Array(100).keys()];

// const xaxis = [x-data];
// const yaxis = [y-data];

const data = {
  labels: xaxis,
  datasets: [{
    label: 'name of line',
    backgroundColor: 'rgb(255, 99, 132)',
    borderColor: 'rgb(255, 99, 132)',
    data: yaxis,
  }]
};

const config = {
  type: 'line',
  data: data,
  options: {}
};

const myChart = new Chart(
document.getElementById('myChart'),
config
);

