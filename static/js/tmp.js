// 折线图
var option = {
    // 修改两条线的颜色
    color: ["#1089E7", "#F57474", "#56D0E3", "#F8B448", "#8B78F6"],
    tooltip: {
        trigger: 'axis'
    },
    /*
    // 图例组件
    legend: {
        // 当serise 有name值时， legend 不需要写data
        // 修改图例组件文字颜色
        textStyle: {
            color: '#4c9bfd'
        },
        right: '10%',
    },*/
    grid: {
        top: '20%',
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true,
        show: true,
        borderColor: '#012f4a'
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['2014', '2015', '2016', '2017', '2018', '2019', '2020'],
        // 去除刻度线
        axisTick: {
            show: false
        },
        // x轴文本颜色
        axisLabel: {
            color: "#4c9bfb"
        },
        // 去除轴线
        axisLine: {
            show: false
        }
    },
    yAxis: {
        type: 'value',
        // 去除刻度线
        axisTick: {
            show: false
        },
        axisLabel: {
            color: "#4c9bfb" // x轴文本颜色
        },
        axisLine: {
            show: false // 去除轴线
        },
        splitLine: {
            lineStyle: {
                color: "#012f4a"
            }
        }
    },
    series: [{
        name: '栖霞区',
        type: 'line',
        smooth: true,
        data: [20, 40, 50, 60, 70, 90, 100]
    }, {
        name: '玄武区',
        type: 'line',
        smooth: true,
        data: [40, 60, 80, 95, 115, 135, 150]
    }, {
        name: '秦淮区',
        type: 'line',
        smooth: true,
        data: [60, 80, 100, 130, 160, 200, 230]
    }, {
        name: '鼓楼区',
        type: 'line',
        smooth: true,
        data: [30, 45, 60, 75, 90, 105, 120]
    }, {
        name: '江宁区',
        type: 'line',
        smooth: true,
        data: [35, 53, 71, 89, 107, 125, 143]
    }, ]
};