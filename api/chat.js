export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ ok: false, error: 'Method not allowed' });
  }

  try {
    const { messages } = req.body;
    if (!messages || !Array.isArray(messages)) {
      return res.status(400).json({ ok: false, error: 'Missing messages array' });
    }

    const apiKey = 'sk-42eca51044284a3abb920672112a176e';

    const response = await fetch('https://api.deepseek.com/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`,
      },
      body: JSON.stringify({
        model: 'deepseek-chat',
        messages: messages,
        temperature: 0.85,
        top_p: 0.9,
        max_tokens: 512,
      }),
    });

    if (!response.ok) {
      const err = await response.text();
      return res.status(response.status).json({ ok: false, error: err });
    }

    const data = await response.json();
    const content = data.choices?.[0]?.message?.content || '';

    return res.status(200).json({ ok: true, content });
  } catch (e) {
    return res.status(500).json({ ok: false, error: e.message });
  }
}
