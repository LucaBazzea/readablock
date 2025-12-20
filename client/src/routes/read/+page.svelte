<script>
  let sentences = [
    "Un gatto aveva fatto conoscenza con un topo e gli aveva tanto vantato il grande amore e l'amicizia che gli portava, che alla fine il topo acconsentì ad abitare con lui; avrebbero governato insieme la casa.",
    "\"Ma per l'inverno dobbiamo provvedere, altrimenti patiremo al fame,\" disse il gatto, \"e tu, topolino, non puoi arrischiarti dappertutto sennò finirai col cadermi in trappola!\"",
    "Il buon consiglio fu seguito e comprarono un pentolino di strutto.",
    "Ma non sapevano dove metterlo; finalmente, pensa e ripensa, il gatto disse: \"Non so dove potrebbe essere più al sicuro che in chiesa; là nessuno osa commettere un furto: lo mettiamo sotto l'altare e non lo tocchiamo prima di averne bisogno.\""
  ];

  const splitWords = (sentence) => {
    return sentence.split(/(\s+)/);
  };

  const handleWordClick = (word) => {
    alert(`You clicked: "${word}"`);
  };

  const handleTranslate = (sentence) => {
    alert(`Translate: "${sentence}"`);
  };
</script>

<div class="min-h-screen bg-base-100 text-base-content">
  <div class="overflow-x-auto">
    <table class="table w-full border-collapse">
      <tbody>
        {#each sentences as sentence, index}
          <tr>
            <td class="border border-base-300 px-2 py-0">
              {#each splitWords(sentence) as part}
                {#if part.trim().length > 0}
                  <button
                    class="btn btn-ghost btn-xs normal-case p-0 m-0.5 hover:bg-base-300"
                    on:click={() => handleWordClick(part)}
                  >
                    {part}
                  </button>
                {:else}
                  {part}
                {/if}
              {/each}
            </td>
            <td class="border border-base-300">
              <button
                on:click={() => handleTranslate(sentence)}
              >
                ⬇️
              </button>
            </td>
          </tr>
        {/each}
      </tbody>
    </table>
  </div>
</div>

