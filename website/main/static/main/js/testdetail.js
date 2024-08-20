(function () {
    "use strict";

    /* basic line chart */
    var options = {
        series: [{
            name: "Test Result",
            data: [88, 104, 78, 90, 59, 65, 68]
        }],
        chart: {
            height: 320,
            type: 'line',
            zoom: {
                enabled: false
            }
        },
        colors: ['#845adf'],
        dataLabels: {
            enabled: false
        },
        stroke: {
            curve: 'straight',
            width: 3,
        },
        grid: {
            borderColor: '#f2f5f7',
        },
        title: {
            text: 'Serum Trigliceride Result Trend',
            align: 'left',
            style: {
                fontSize: '13px',
                fontWeight: 'bold',
                color: '#8c9097'
            },
        },
        xaxis: {
            categories: ['Nov 2020', 'June 2021', 'Aug 2021', 'Sep 2021', 'Aug 2022', 'April 2023', 'Jan 2024'],
            labels: {
                show: true,
                style: {
                    colors: "#8c9097",
                    fontSize: '11px',
                    fontWeight: 600,
                    cssClass: 'apexcharts-xaxis-label',
                },
            }
        },
        yaxis: {
            labels: {
                show: true,
                style: {
                    colors: "#8c9097",
                    fontSize: '11px',
                    fontWeight: 600,
                    cssClass: 'apexcharts-yaxis-label',
                },
            }
        }
    };
    var chart = new ApexCharts(document.querySelector("#line-chart"), options);
    chart.render();
})();