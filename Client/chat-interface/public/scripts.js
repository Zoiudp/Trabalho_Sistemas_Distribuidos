document.getElementById('uploadForm').addEventListener('submit', async function (e) {
    e.preventDefault(); // Evita o envio padrão do formulário
  
    const text = document.getElementById('text').value;
    const photo = document.getElementById('photo').files[0];
  
    if (!text || !photo) {
      alert('Por favor, preencha o texto e selecione uma foto.');
      return;
    }
  
    const formData = new FormData();
    formData.append('text', text);
    formData.append('photo', photo);
  
    try {
      const response = await fetch('http://localhost:5000/api/upload', {
        method: 'POST',
        body: formData,
      });
  
      if (!response.ok) {
        throw new Error('Erro ao enviar os dados');
      }
  
      const result = await response.json();
      document.getElementById('responseMessage').textContent = `Dados enviados com sucesso: ${result.message}`;
    } catch (error) {
      console.error('Erro:', error);
      document.getElementById('responseMessage').textContent = 'Erro ao enviar os dados.';
    }
  });
  