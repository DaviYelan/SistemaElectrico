function generatePDF() {
    var canvas = document.getElementById('myChart');
    var imgData = canvas.toDataURL('image/png');

    var pdf = new jsPDF();
    pdf.addImage(imgData, 'PNG', 10, 10, 180, 100);
    pdf.save('grafica.pdf');
}